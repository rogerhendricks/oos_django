from django.db import models as db
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class Device(db.Model):
    __tablename__= "device" # table name

    dev_man_choices = (
    ('Abbot','Abbot'),
    ('Biotronik','Biotronik'),
    ('Boston Scientific','Boston Scientific'),
    ('Medtronic','Medtronic'),
    ('Sorin','Sorin'),
    )

    dev_type_choices = (
    ('Pacemaker','Pacemaker'),
    ('Defibrillator','Defibrillator'),
    )
    # columns!
    id = db.AutoField(primary_key=True)
    device_man=db.CharField(max_length=30, choices=dev_man_choices, null=True)
    device_name=db.CharField(max_length=30, null=True)
    device_type=db.CharField(max=15, choices=dev_type_choices, null=True)
    implant_date=db.DateField(null=True)
    bol_voltage = db.DecimalField(max_digits=3, decimal_places=2, null=True)
    eri_voltage = db.DecimalField(max_digits=3, decimal_places=2, null=True)

    def get_absolute_url(self):
        return reverse('device:detail', kwargs={"pk": self.pk})

    def __str__(self):
        return '%s %s %s' % ( self.device_man, self.device_name, self.device_type)



class Lead(db.Model):
    __tablename__= "lead" # table name

    lead_man_choices = (
    ('Abbot','Abbot'),
    ('Biotronik','Biotronik'),
    ('Boston Scientific','Boston Scientific'),
    ('Medtronic','Medtronic'),
    ('Sorin','Sorin'),
    )

    lead_placement_choices = (
        ('RA', 'Right Atrium'),
        ('RV', 'Right Ventricle'),
        ('LV', 'Left Ventricle'),
    )
    # columns!
    id = db.AutoField(primary_key=True)
    lead_man=db.CharField(max_length=30, choices=lead_man_choices, null=True)
    lead_name=db.CharField(max_length=30, null=True)
    implant_date=db.DateField(null=True)
    lead_serial=db.CharField(max_length=30, null=True)
    lead_type=db.CharField(max=10, null=True)
    lead_placement=db.CharField(max=30, choices=lead_placement_choices ,null=True)

    def __str__(self):
        return '%s %s %s' % ( self.lead_man, self.lead_name, self.lead_placement)