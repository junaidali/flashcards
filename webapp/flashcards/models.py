from django.db import models

# Create your models here.
class Category(models.Model):
    name_en = models.CharField(max_length=512)
    name_ar = models.CharField(max_length=512)
    description_en = models.TextField(max_length=1024, blank=True)
    description_ar = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return 'Name (EN): %s, Name (AR): %s' %(self.name_en, self.name_ar)

    class Meta:
        verbose_name_plural = "categories"

class Word(models.Model):
    en = models.CharField(max_length=1024)
    ar = models.CharField(max_length=1024)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.en