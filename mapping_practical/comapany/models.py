from django.db import models

# Create your models here.


class employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table = 'employee_master'

def get_supervior_name():
    return employee.objects.filter(name='Admin').first()   



class address(models.Model):
    city = models.CharField(max_length=30)
    pin = models.IntegerField()
    emp = models.ForeignKey(employee,on_delete=models.SET(get_supervior_name))

    class Meta:
        db_table = 'address_master'