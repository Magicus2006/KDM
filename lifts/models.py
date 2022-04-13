from django.db import models

# Create your models here.
# EQ("="), GTE(">="), GT(">"), LT("<"), LTE("<=");

class NameBrend(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class LiftType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tipon = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=45, unique=True)
    smallName = models.CharField(max_length=25)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol

class VendorCode(models.Model):
    vendorCode = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    cost = models.BigIntegerField(default=0)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.vendorCode

# Модель для хранения данных подъемников по индексу
class CalculationTable(models.Model):
    indexFrom = models.IntegerField()
    indexTo = models.IntegerField()
    heightFacadeFrom = models.IntegerField()
    heightFacadeTo = models.IntegerField()
    vendorCode = models.ForeignKey(
        VendorCode,
        on_delete=models.SET_NULL,
        null=True,
    )
    liftType = models.ForeignKey(
        LiftType,
        on_delete=models.SET_NULL,
        null=True,
    )
    nameBrand = models.ForeignKey(
        NameBrend,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f'{self.nameBrand.name} Индекс ({self.indexFrom}-{self.indexTo}) Фасад({self.heightFacadeFrom}-{self.heightFacadeTo}) {self.vendorCode.vendorCode}'

# Модель для хранения данных подъемников по весу
class CalculationTableWeightFacade(models.Model):
    weightFacadeFrom = models.DecimalField(max_digits=5, decimal_places=2)
    weightFacadeTo =  models.DecimalField(max_digits=5, decimal_places=2)
    heightFacadeFrom = models.IntegerField()
    heightFacadeTo = models.IntegerField()
    vendorCode = models.ForeignKey(
        VendorCode,
        on_delete=models.SET_NULL,
        null=True,
    )
    liftType = models.ForeignKey(
        LiftType,
        on_delete=models.SET_NULL,
        null=True,
    )
    nameBrand = models.ForeignKey(
        NameBrend,
        on_delete=models.SET_NULL,
        null=True,
    )
    def __str__(self):
        return f'{self.nameBrand.name} Вес ({self.weightFacadeFrom}-{self.weightFacadeTo}) Фасад({self.heightFacadeFrom}-{self.heightFacadeTo}) {self.vendorCode.vendorCode}'
