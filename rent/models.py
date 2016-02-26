from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    vat_code = models.CharField(max_length=100)
    ssn = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    driving_licence = models.CharField(max_length=100)


# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    plate = models.CharField(max_length=12)
    miles = models.IntegerField()

    def __str__(self):
        return "{Name: '" + str(self.name) + " plate " + str(self.plate) + " cur km " + str(self.miles) + "}"


class Contract(models.Model):
    customer = models.ForeignKey(Customer)
    vehicle = models.ForeignKey(Vehicle)
    contract_start = models.DateTimeField()
    contract_expected_end = models.DateTimeField()
    contract_real_end = models.DateTimeField()
    miles_in = models.IntegerField()
    miles_out = models.IntegerField()


class Invoice(models.Model):
    contract = models.ForeignKey(Contract)
    invoice_number = models.IntegerField()
    invoice_date = models.DateTimeField()
    invoice_total = models.DecimalField(max_digits=12, decimal_places=2)
    is_payed = models.BooleanField(default = False)
    date_payed = models.DateTimeField()
