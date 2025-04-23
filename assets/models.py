from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Library(CommonInfo):
    name = models.CharField(max_length=3)
    description = models.CharField(max_length=133)
    url = models.URLField()

    def __str__(self):
        return self.name


class LibrarySeller(CommonInfo):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=12)
    url = models.URLField()

    def __str__(self):
        return self.name


class LibraryItem(CommonInfo):
    class AgeRatingChoices(models.TextChoices):
        MATURE = "M", _("Mature")
        NOT_MATURE = "NM", _("Not Mature")

    class LicenseTermsChoices(models.TextChoices):
        OTHER_LICENSE = "Ol", _("Other License")
        STANDARD_LICENSE = "SL", _("Standard License")

    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=18)
    url = models.URLField()
    publish_date = models.DateField()
    license_terms = models.CharField(max_length=2, choices=LicenseTermsChoices)
    age_rating = models.CharField(max_length=2, choices=AgeRatingChoices)
    promotional_content = models.BooleanField(default=False)
    allows_usage_with_ai = models.BooleanField(default=False)
    generated_with_ai = models.BooleanField(default=False)

    def __str__(self):
        return self.name
