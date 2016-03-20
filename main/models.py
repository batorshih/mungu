# -*- coding: utf-8 -*-
from django.db import models
from django.utils.html import format_html
from filebrowser.fields import FileBrowseField
# Create your models here.
class Nershil(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class Tamgas(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'tamga', blank=True)
    nershil = models.ManyToManyField(Nershil,blank = True)
    def __unicode__(self):
		return self.name
    def getimage(self):
        return format_html('<img height="100"  src="/assets/%s" />' % self.image.name)
    def nershiluud(self):
        return "\n".join([p.name for p in self.nershil.all()])
    class Meta:
        verbose_name = u"тамга-"
        



class aimag_city(models.Model):
    name = models.CharField(max_length=50, verbose_name='хот аймаг')
    is_country=models.CharField(max_length=1,choices=(('1','tiim'),('0','hudal')),default='1')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u"location аймаг"
        verbose_name_plural = u"location аймаг"

class soum_district(models.Model):
    name = models.CharField(max_length=50, verbose_name='сум дүүрэг')
    aim= models.ForeignKey(aimag_city,null=True)
    def __unicode__(self):
        return self.name;
    class Meta:
        verbose_name = u"location сум"
        verbose_name_plural = u"location сум"

class bag_khoroo(models.Model):
    name = models.CharField(max_length=50, verbose_name='баг хорооо')
    soum= models.ForeignKey(soum_district,null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u"location баг"
        verbose_name_plural = u"location баг"

