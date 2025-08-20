from django.db import models
from django.contrib.auth.models import User

WEEKDAYS_LiST = (
    ("Mon", "Monday"),
    ("Tue", "Tuesday"),
    ("Wed", "Wednesday"),
    ("Thu", "Thursday"),
    ("Fri", "Friday"),
    ("Sat", "Saturday"),
    ("Sun", "Sunday"),
)
class WorkingDays(models.Model):
    day = models.CharField(max_length=3, choices=WEEKDAYS_LiST)
    startHour = models.TimeField()
    endHour =models.TimeField()

    def __str__(self):
        return str(self.day + " " + str(self.startHour) + " - " + str(self.endHour))



class Service(models.Model):
    name = models.CharField(max_length=100)
    target = models.CharField(max_length=3, default=100)
    working_schedule = models.ManyToManyField(WorkingDays)


    def __str__(self):
        return self.name

class rtm_comment(models.Model):

    comm_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    comm_body = models.TextField()
    comm_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comm_timestamp = models.DateTimeField()



    def __str__(self):
        return str(str(self.comm_timestamp)+ " - "+str(self.comm_service) + " - " + str(self.comm_body)+ " - " + str(self.comm_author))

class Rap30(models.Model):
    interval = models.DateTimeField(db_column='Interval', primary_key=True)  # Field name made lowercase. The composite primary key (Interval, Service) found, that is not supported. The first column is selected.
    service = models.TextField(db_column='Service')  # Field name made lowercase.
    forecast = models.IntegerField(db_column='Forecast', blank=True, null=True)  # Field name made lowercase.
    real = models.IntegerField(db_column='Real', blank=True, null=True)  # Field name made lowercase.
    thr = models.IntegerField(db_column='Thr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rap_30'
        unique_together = (('interval', 'service'),)
        