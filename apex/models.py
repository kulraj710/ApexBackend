from django.db import models

# Create your models here.

# patient profile model
class PatProfile(models.Model):
    uid = models.CharField(primary_key=True, max_length=20)
    f_name = models.CharField(max_length=25, blank=True, null=True)
    l_name = models.CharField(max_length=25, blank=True, null=True)
    dob = models.DateField()
    parent_name = models.CharField(max_length=55, blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    sex = models.CharField(max_length=3, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    referred_by = models.CharField(max_length=3, blank=True, null=True) 
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'pat_profile'
    
    def __str__(self):
        return self.f_name


# opd model
class OpdRecord(models.Model):
    date = models.DateTimeField()
    weight = models.CharField(max_length=11, blank=True, null=True)
    height = models.CharField(max_length=15, blank=True, null=True)
    temp = models.CharField(max_length=5, blank=True, null=True)
    ref = models.ForeignKey('PatProfile', on_delete=models.CASCADE, db_column='ref')
    id = models.AutoField(primary_key=True)
    charge = models.IntegerField()

    class Meta:
        db_table = 'opd_record'
        unique_together = ('ref', 'id')
    
    # def __str__(self):
    #     return self.ref

