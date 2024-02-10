from django.db import models

class Product(models.Model):
    pid=models.CharField(max_length=10)
    pname=models.CharField(max_length=10)
    pcost=models.DecimalField(max_digits=10,decimal_places=2)
    pmfdt=models.DateField()
    pexpdt=models.DateField()

