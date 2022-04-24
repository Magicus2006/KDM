from django.db import models

# Create your models here.
# EQ("="), GTE(">="), GT(">"), LT("<"), LTE("<=");

class NameBrend(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class LiftType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tipon = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тип подъемника'
        verbose_name_plural = 'Типы подъемников'

class Currency(models.Model):
    name = models.CharField(max_length=45, unique=True)
    smallName = models.CharField(max_length=25)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

# Артикулы
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
    class Meta:
        verbose_name = 'Артикулы'
        verbose_name_plural = 'Артикулы'

# Модель для хранения данных подъемников по индексу
class CalculationTable(models.Model):
    indexFrom = models.IntegerField(verbose_name="Индекс от")
    indexTo = models.IntegerField(verbose_name="Индекс до")
    heightFacadeFrom = models.IntegerField(verbose_name="Высота от")
    heightFacadeTo = models.IntegerField(verbose_name="Высота до")
    vendorCode = models.ForeignKey(
        VendorCode,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Артикул"
    )
    liftType = models.ForeignKey(
        LiftType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Тип подъемника"
    )
    nameBrand = models.ForeignKey(
        NameBrend,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Производитель"
    )
    display = models.BooleanField(verbose_name="Показывать", default=False)

    class Meta:
        verbose_name = 'Подъемники по индексу'
        verbose_name_plural = 'Подъемники по индексу'

    def __str__(self):
        return f'{self.nameBrand.name} Индекс ({self.indexFrom}-{self.indexTo}) Фасад({self.heightFacadeFrom}-{self.heightFacadeTo}) {self.vendorCode.vendorCode}'

# Модель для хранения данных подъемников по весу
class CalculationTableWeightFacade(models.Model):
    weightFacadeFrom = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Вес от")
    weightFacadeTo =  models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Вес до")
    heightFacadeFrom = models.IntegerField(verbose_name="Высота от")
    heightFacadeTo = models.IntegerField(verbose_name="Высота до")
    vendorCode = models.ForeignKey(
        VendorCode,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Артикул",
    )
    liftType = models.ForeignKey(
        LiftType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Тип подъемника",
    )
    nameBrand = models.ForeignKey(
        NameBrend,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Производитель",
    )
    display = models.BooleanField(verbose_name="Показывать", default=False)

    class Meta:
        verbose_name = 'Подъемники по весу'
        verbose_name_plural = 'Подъемники по весу'

    def __str__(self):
        return f'{self.nameBrand.name} Вес ({self.weightFacadeFrom}-{self.weightFacadeTo}) Фасад({self.heightFacadeFrom}-{self.heightFacadeTo}) {self.vendorCode.vendorCode}'
