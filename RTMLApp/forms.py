import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import rtm_comment, Service


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Enter Username", widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput(attrs={"class":"form-control"}))

class AddComment(forms.ModelForm):
    class Meta:
        model = rtm_comment
        fields = ["comm_service","comm_body"]
        labels = {"comm_service":"Service","comm_body":"Text"}
        widgets = {"comm_service":forms.Select(attrs={"class": "btn btn-outline-success input-group mb-2"}),
                   "comm_body": forms.Textarea(attrs={"class":"input-group mb-2"})}

class FilterForm(forms.ModelForm):
    class Meta:
        model = rtm_comment
        fields = ["comm_service","comm_timestamp"]
        labels = {"comm_service":"Service","comm_timestamp":"Data"}
        widgets = {"comm_service":forms.Select(attrs={"class": "btn btn-outline-success",
                                                      "style":"width:200px"}),
                   "comm_timestamp":DatePickerInput(attrs={"class":"btn btn-outline-success",
                                                           "value": datetime.date.today(),
                                                           "data-date-format": "DD/MM/yyyy",
                                                           })}