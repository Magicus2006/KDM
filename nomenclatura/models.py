from django.db import models

# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=40)
    parent = models.ForeignKey("self",
                               verbose_name="Родиельская папка",
                               blank=True,
                               null=True,
                               related_name="folder_children",
                               on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Nomenclatura(models.Model):
    article = models.CharField(max_length=40)
    name = models.CharField(max_length=120)
    parent = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.article+" "+self.name
