from django.db import models as db
from django.urls import reverse


class Doc(db.Model):
    __tablename__= "doc"
    doc_type_choices = (
        ('Surgeon','Surgeon'),
        ('Cardiologist','Cardiologist'),
        ('General Practitioner','General Practitioner'),
    )

    id = db.AutoField(primary_key=True)
    first_name = db.CharField(max_length=30)
    last_name = db.CharField(max_length=30)
    address = db.CharField(max_length=120, null=True)
    phone_1 = db.PositiveIntegerField(null=True)
    phone_2 = db.PositiveIntegerField(null=True)
    email = db.EmailField(max_length=120, null=True)
    doc_type = db.CharField(max_length=30, choices=doc_type_choices, null=True)
    #clients = db.ManyToManyField(Client)

    class Meta:
        ordering = ('-last_name',)


    #def __str__(self):
    #    return '%s %s %s' % ( self.doc_type, self.first_name, self.last_name )
    def __str__(self):
        return '%s %s %s' % ( self.doc_type, self.first_name, self.last_name )



class Client(db.Model):
    __tablename__= "clients" # table name

    dev_man_choices = (
    ('Abbot','Abbot'),
    ('Biotronik','Biotronik'),
    ('Boston Scientific','Boston Scientific'),
    ('Medtronic','Medtronic'),
    ('Sorin','Sorin'),
    )
    # columns!
    id = db.AutoField(primary_key=True)
    first_name = db.CharField(max_length=30)
    last_name = db.CharField(max_length=30)
    dob = db.DateField()
    record_number = db.PositiveIntegerField(null=True)
    device_man=db.CharField(max_length=30, choices=dev_man_choices, null=True)
    device_name=db.CharField(max_length=30, null=True)
    implant_date=db.DateField(null=True)
    device_serial=db.CharField(max_length=30, null=True)
    bol_voltage = db.DecimalField(max_digits=3, decimal_places=2, null=True)
    eri_voltage = db.DecimalField(max_digits=3, decimal_places=2, null=True)
    doctors = db.ManyToManyField(Doc)


    def get_absolute_url(self):
        return reverse('client:detail', kwargs={"pk": self.pk})


    def __str__(self):
        return '%s %s' % ( self.record_number, self.last_name )


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

