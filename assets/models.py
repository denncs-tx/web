from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _


# TODO: Model Description & Included formats sections
# Create your models here.
class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(CommonInfo):
    name = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Library(CommonInfo):
    name = models.CharField(max_length=3)
    description = models.CharField(max_length=133)
    url = models.URLField()

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'

    def __str__(self):
        return self.name


class LibrarySeller(CommonInfo):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=12)
    url = models.URLField()

    class Meta:
        verbose_name = 'Library Seller'

    def __str__(self):
        return self.name


class LibraryItem(CommonInfo):
    class AgeRatingChoices(models.TextChoices):
        MATURE = "M", _("Mature")
        NOT_MATURE = "NM", _("Not Mature")

    class DistributionMethodChoices(models.TextChoices):
        ASSET_PACKAGE = "AP", _("Asset Package")
        COMPLETE_PROJECT = "CP", _("Complete Project")
        PLUGIN = "PL", _("Plugin")

    class LicenseTermsChoices(models.TextChoices):
        OTHER_LICENSE = "Ol", _("Other License")
        STANDARD_LICENSE = "SL", _("Standard License")

    source_library = models.ForeignKey(Library, on_delete=models.CASCADE)
    library_seller = models.ForeignKey(LibrarySeller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=18)
    url = models.URLField()
    publish_date = models.DateField()
    license_terms = models.CharField(max_length=2, choices=LicenseTermsChoices)
    age_rating = models.CharField(max_length=2, choices=AgeRatingChoices)
    promotional_content = models.BooleanField(default=False)
    allows_usage_with_ai = models.BooleanField(verbose_name="Allows usage with AI", default=False)
    generated_with_ai = models.BooleanField(verbose_name="Generated with AI", default=False)
    description = models.TextField()
    additional_notes = models.TextField()
    max_ue_version = models.DecimalField(max_digits=4, decimal_places=2)
    target_windows = models.BooleanField(default=False)
    target_linux = models.BooleanField(default=False)
    target_mac = models.BooleanField(default=False)
    target_win32 = models.BooleanField(default=False)
    target_android = models.BooleanField(default=False)
    target_ios = models.BooleanField(default=False)
    last_updated = models.DateField()
    distribution_method = models.CharField(max_length=2, choices=DistributionMethodChoices.choices)
    documentation_url = models.URLField()

    class Meta:
        verbose_name = 'Library Item'
        verbose_name_plural = 'Library Items'

    def __str__(self):
        return self.name


class LibraryItemLink(CommonInfo):
    library_item = models.ForeignKey(LibraryItem, on_delete=models.CASCADE)
    friendly_name = models.CharField(max_length=58)
    url = models.URLField()

    class Meta:
        verbose_name = 'Additional URL'
        verbose_name_plural = 'Additional URLs'

    def __str__(self):
        return self.friendly_name
