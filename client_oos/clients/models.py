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
        return '%s %s' % (self.record_number, self.last_name )


class Oos(db.Model):
    __tablename__ = "oos"

    oos_type_choices = (
        ('In Clinic Periodic', 'In Clinic Periodic'),
        ('In Clinic Call Back','In Clinic Call Back'),
        ('Remote Periodic','Remote Periodic'),
        ('Remote Early Detection','Remote Early Detection'),
    )

    # columns!
    id = db.AutoField(primary_key=True)
    content = db.TextField(max_length=500)
    oos_type = db.CharField(max_length=25, choices=oos_type_choices, default='In Clinic Periodic')
    batt_volt = db.DecimalField(max_digits=4, decimal_places=2)
    oos_date = db.DateTimeField()
    client = db.ForeignKey('Client', on_delete=db.CASCADE)

    class Meta:
        ordering = ('-oos_date',)

    def get_absolute_url(self):
        return reverse('client:service_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.oos_type
