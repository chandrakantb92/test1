from django.db import models
from django.db import connections



# Create your models here.
class Model1(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'model1'
        
# models.py


class Employee(models.Model):
    name = models.CharField(max_length=100)
    pan = models.CharField(max_length=10)
    # Add other relevant fields for employee details

    def __str__(self):
        return self.name

class TDSRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    financial_year = models.IntegerField()
    quarter = models.IntegerField()
    tds_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other relevant fields for TDS record

    def __str__(self):
        return f"{self.employee.name} - FY: {self.financial_year} Q: {self.quarter}"
