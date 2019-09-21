from django.db import models as db
from django.urls import reverse
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator


class Doc(db.Model):
    __tablename__= "doc"
    doc_type_choices = (
        ('Surgeon','Surgeon'),
        ('Cardiologist','Cardiologist'),
        ('General Practitioner','General Practitioner'),
    )
    state_choices = (
        ('New South Wales','New South Wales'),
        ('Queensland','Queensland'),
        ('Victoria','Victoria'),
        ('Canberra','Canberra'),
        ('Northern Territory','Northern Territory'),
        ('Western Australia','Western Australia'),
        ('South Australia','South Australia'),
    )

    id = db.AutoField(primary_key=True)
    first_name = db.CharField(max_length=30)
    last_name = db.CharField(max_length=30)
    str_address = db.CharField(max_length=120, null=True)
    ct_address = db.CharField(max_length=120, null=True)
    pc_address = db.PositiveIntegerField(null=True)
    st_address = db.CharField(max_length=30, choices=state_choices, null=True)
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
    batt_chg_time = db.DecimalField(max_digits=4, decimal_places=2, null=True)
    oos_date = db.DateTimeField()
    paced_percent_ra = db.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    paced_percent_rv = db.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    paced_percent_lv = db.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    intra_amp_ra = db.DecimalField(max_digits=4, decimal_places=2, null=True)
    pace_imp_ra = db.IntegerField(validators=[MinValueValidator(150), MaxValueValidator(3000)], null=True)
    pace_thr_ra = db.DecimalField(max_digits=4, decimal_places=2, null=True)
    pace_thr_pw_ra = db.DecimalField(max_digits=4, decimal_places=2, null=True)
    intra_amp_rv = db.DecimalField(max_digits=4, decimal_places=2, null=True)
    pace_imp_rv = db.IntegerField(validators=[MinValueValidator(150), MaxValueValidator(3000)], null=True)
    pace_thr_rv = db.DecimalField(max_digits=4, decimal_places=2, null=True)
    pace_thr_pw_rv = db.DecimalField(max_digits=4, decimal_places=2, null=True)
    shock_imp_rv = db.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)], null=True)
    shock_imp_svc = db.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)], null=True)
    client = db.ForeignKey('Client', on_delete=db.CASCADE)

    class Meta:
        ordering = ('-oos_date',)

    def get_absolute_url(self):
        return reverse('client:service_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.oos_type


class Procedure(db.Model):
    __tablename__ = "procedure"

    procedure_type_choices = (
        ('Ischaemic VT Ablation', 'Ischaemic VT Ablation'),
        ('Idiopathic VT Ablation', 'Idiopathic VT Ablation'),
        ('Pulmonary Vein Isolation','Pulmonary Vein Isolation'),
        ('SVT Ablation','SVT Ablation'),
        ('Diagnostic','Diagnostic'),
    )

    # columns!
    id = db.AutoField(primary_key=True)
    content = db.TextField(max_length=500)
    procedure_type = db.CharField(max_length=50, choices=procedure_type_choices, default='Diagnostic')
    procedure_date = db.DateTimeField()
    client = db.ForeignKey('Client', on_delete=db.CASCADE)

    class Meta:
        ordering = ('-procedure_date',)

    def get_absolute_url(self):
        return reverse('client:procedure_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.procedure_type
