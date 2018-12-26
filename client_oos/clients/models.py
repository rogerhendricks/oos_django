from django.db import models as db
from django.urls import reverse


class Client(db.Model):
    __tablename__= "clients" # table name

    # columns!
    id = db.AutoField(primary_key=True)
    first_name = db.CharField(max_length=30)
    last_name = db.CharField(max_length=30)
    dob = db.DateField()
    record_number = db.PositiveIntegerField(null=True)

    def get_absolute_url(self):
        return reverse('client:detail', kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.last_name


class Oos(db.Model):
    __tablename__ = "oos"

    # columns!
    id = db.AutoField(primary_key=True)
    content = db.TextField(max_length=500)
    oos_type = db.CharField(max_length=25)
    batt_volt = db.DecimalField(max_digits=4, decimal_places=2)
    oos_date = db.DateTimeField(auto_now_add=True)
    client = db.ForeignKey('Client', on_delete=db.CASCADE)

    class Meta:
        ordering = ('oos_date',)

    def get_absolute_url(self):
        return reverse('client:detail', kwargs={"pk" : self.pk})

    def __str__(self):
        return self.oos_type
        
