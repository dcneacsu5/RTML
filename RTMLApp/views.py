from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, AddComment, FilterForm
from .models import rtm_comment, Service, WorkingDays, Rap30
import datetime
import pandas as pd



# Create your views here.
def login_req(request):
    if request.method=="POST":
        form=LoginForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("RTMLApp:home")

    form=LoginForm()
    return render(request, "RTMLApp/login.html", {"form":form})

def logout_req(request):
    logout(request)
    return redirect("RTMLApp:home")


@login_required(redirect_field_name="")
def home(request):
    wd = None
    serv = None
    kpi_df = pd.DataFrame(columns=['interval', 'service', 'SL', 'Deviatie', 'forecast', 'real', 'thr'])
    interval_dict = {}
    comm_list = None
    AddForm = AddComment()
    ff = FilterForm(request.GET)
    #GET logic
    if request.method == "GET":
        selected_service = request.GET.get("comm_service")
        selected_date = request.GET.get("comm_timestamp")
        
        
        if selected_service != None:
            comm_list = rtm_comment.objects.filter(comm_service=selected_service,
                                                   comm_timestamp__date=selected_date)
            serv = Service.objects.get(id=selected_service)
            wd = WorkingDays.objects.filter(service__id=selected_service)

            qs = Rap30.objects.using("kpi").filter(interval__date=selected_date, service=serv)
            if qs.exists():
                kpi_df = pd.DataFrame.from_records(qs.values())
                sl_col = kpi_df["thr"]/kpi_df["real"]
                dev_col = (kpi_df["real"]-kpi_df["forecast"])/kpi_df["forecast"]
                kpi_df.insert(2,"SL", sl_col)
                kpi_df.insert(3,"Deviatie", dev_col)
            
            #get working intervals and fill the dictionary
            for d in wd:
                if datetime.datetime.strftime(datetime.datetime.fromisoformat(selected_date),"%a") == d.day:
                    add_interval = datetime.timedelta(minutes=30)
                    current_interval = datetime.datetime.combine(datetime.datetime.fromisoformat(selected_date),d.startHour)
                    last_interval = datetime.datetime.combine(datetime.datetime.fromisoformat(selected_date),d.endHour) - add_interval
                    
                    while last_interval.strftime("%H:%M") not in interval_dict.keys():
                        interval_comm = []
                        for c in comm_list:
                            if current_interval < c.comm_timestamp < (current_interval+add_interval):
                                interval_comm.append(c.comm_timestamp.strftime("%H:%M")+ " - " + str(c.comm_author) + " : " + c.comm_body)
                        interval_dict[current_interval.strftime("%H:%M")] = [kpi_df["SL"].values.round(2)*100,
                                                                         kpi_df["Deviatie"].values.round(3)*100,
                                                                         kpi_df["forecast"].values,
                                                                         kpi_df["real"].values,
                                                                         kpi_df["thr"].values,
                                                                         serv.target,
                                                                         interval_comm]
                        current_interval = current_interval + add_interval

    # Add comment Form logic
    elif request.method == "POST":
        serv = Service.objects.get(id=request.POST.get("comm_service"))
        wd = WorkingDays.objects.filter(service=serv)
        for d in wd:
            if datetime.datetime.strftime(datetime.datetime.now(),"%a") == d:
                print(serv)
        AddForm = AddComment(request.POST)
        if AddForm.is_valid():
            AddForm.instance.comm_author = request.user
            AddForm.instance.comm_timestamp = datetime.datetime.now()
            AddForm.save()
            return redirect(request.META['HTTP_REFERER'])

    return render(request=request, template_name="RTMLApp/index.html", context={"AddForm":AddForm,
                                                                                "ff":ff,
                                                                                "comm_list":comm_list,
                                                                                "serv":serv,
                                                                                "wd":wd,
                                                                                "interval_dict":interval_dict
                                                                                })
