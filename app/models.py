from django.db import models


# Create your models here.
class MenuNames(models.Model):
    name = models.CharField('Menu name', max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    name = models.CharField('Item name', max_length=50, blank=False, null=False)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='Parent', related_name='children')
    menu = models.ForeignKey('MenuNames', blank=False, null=False)
    url = models.CharField('Item href', max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name