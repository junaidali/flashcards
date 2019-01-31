from django.db import models

# Create your models here.
class Category(models.Model):
    name_primary = models.CharField(max_length=512)
    name_secondary = models.CharField(max_length=512)
    description_primary = models.TextField(max_length=1024, blank=True)
    description_secondary = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return 'Name (Primary): %s, Name (Secondary): %s' %(self.name_primary, self.name_secondary)

    class Meta:
        verbose_name_plural = "categories"

class Tag(models.Model):
    tag_primary = models.CharField(max_length=1024)
    tag_secondary = models.CharField(max_length=1024)

    def __str__(self):
        return self.tag_primary

class Word(models.Model):
    word_primary = models.CharField(max_length=1024)
    word_secondary = models.CharField(max_length=1024)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.word_primary

    