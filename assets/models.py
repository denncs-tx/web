from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(CommonInfo):
    name = models.CharField(max_length=22, unique=True, null=False, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Library(CommonInfo):
    name = models.CharField(max_length=3, unique=True, null=False, blank=False)
    description = models.CharField(max_length=133, null=False, blank=True)
    url = models.URLField(unique=True, null=False, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'

    def __str__(self):
        return self.name


class LibrarySeller(CommonInfo):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=24, null=False, blank=False)
    url = models.URLField(null=False, blank=True)

    class Meta:
        ordering = ['library', 'name']
        unique_together = ['library', 'name']
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
        STANDARD_LICENSE = "SL", _("Standard License")
        UE_MARKETPLACE = "UM", _("UE Marketplace")

    class UEVersionChoices(models.TextChoices):
        V4_21 = '4.21', "4.21"
        V4_22 = '4.22', "4.22"
        V4_23 = '4.23', "4.23"
        V4_24 = '4.24', "4.24"
        V4_25 = '4.25', "4.25"
        V4_26 = '4.26', "4.26"
        V4_27 = '4.27', "4.27"
        V5_0 = '5.0', "5.0"
        V5_1 = '5.1', "5.1"
        V5_2 = '5.2', "5.2"
        V5_3 = '5.3', "5.3"
        V5_4 = '5.4', "5.4"
        V5_5 = '5.5', "5.5"

    source_library = models.ForeignKey(Library, on_delete=models.CASCADE)
    library_seller = models.ForeignKey(LibrarySeller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=62, null=False, blank=False)
    url = models.URLField(null=False, blank=False)
    publish_date = models.DateField(null=True, blank=True)
    license_terms = models.CharField(max_length=2, choices=LicenseTermsChoices, null=False, blank=True)
    age_rating = models.CharField(max_length=2, choices=AgeRatingChoices, null=False, blank=True)
    promotional_content = models.BooleanField(default=False)
    allows_usage_with_ai = models.BooleanField(verbose_name="Allows usage with AI", default=False)
    generated_with_ai = models.BooleanField(verbose_name="Generated with AI", default=False)
    description = models.TextField(null=False, blank=True)
    max_ue_version = models.CharField(max_length=4, null=False, blank=True, choices=UEVersionChoices.choices)
    target_android = models.BooleanField(default=False)
    target_gearvr = models.BooleanField(default=False)
    target_hololens2 = models.BooleanField(default=False)
    target_html5 = models.BooleanField(default=False)
    target_ios = models.BooleanField(default=False)
    target_linux = models.BooleanField(default=False)
    target_mac = models.BooleanField(default=False)
    target_nintendo_switch = models.BooleanField(default=False)
    target_oculus = models.BooleanField(default=False)
    target_ps4 = models.BooleanField(default=False)
    target_steamvr_htcvive = models.BooleanField(default=False)
    target_win32 = models.BooleanField(default=False)
    target_windows = models.BooleanField(default=False)
    target_xboxone = models.BooleanField(default=False)
    last_updated = models.DateField(null=True, blank=True)
    distribution_method = models.CharField(max_length=2, choices=DistributionMethodChoices.choices, null=False, blank=True)
    documentation_url = models.URLField(null=False, blank=True)

    class Meta:
        ordering = ['source_library', 'library_seller', 'name']
        unique_together = ['source_library', 'library_seller', 'name']
        verbose_name = 'Library Item'
        verbose_name_plural = 'Library Items'

    def __str__(self):
        return self.name


class LibraryItemLink(CommonInfo):
    library_item = models.ForeignKey(LibraryItem, on_delete=models.CASCADE)
    friendly_name = models.CharField(max_length=58)
    url = models.URLField(null=False, blank=True)

    class Meta:
        unique_together = ['library_item', 'friendly_name']
        verbose_name = 'Additional URL'
        verbose_name_plural = 'Additional URLs'

    def __str__(self):
        return self.friendly_name
