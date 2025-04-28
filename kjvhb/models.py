from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(CommonInfo):
    name = models.CharField(max_length=100)
