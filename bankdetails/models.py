from django.db import models

# Create your models here.


class Bank(models.Model):
    """
    Model containing details of bank
    """
    name = models.CharField(verbose_name="Bank Name", max_length=500)


class Branch(models.Model):
    """
    Model containing info about the branches 
    and a foreign key to main bank
    """
    ifsc = models.CharField("IFSC Code", max_length=500)
    bank_id = models.ForeignKey("Bank", on_delete=models.CASCADE)
    branch = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    favourite = models.BooleanField(default=False)

    class Meta:
        ordering = ["ifsc"]
