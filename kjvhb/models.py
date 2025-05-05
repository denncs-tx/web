from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(CommonInfo):
    name = models.CharField(max_length=5, null=False, blank=False)


class Book(CommonInfo):
    class TestamentChoices(models.TextChoices):
        NT = "NT", _("New Testament")
        OT = "OT", _("Old Testament")

    testament = models.CharField(max_length=2, null=False, blank=False, choices=TestamentChoices)
    full_name = models.CharField(max_length=38, unique=True, null=False, blank=False)
    common_name = models.CharField(max_length=7, unique=True, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    estimated_chapters = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)], null=False)
    estimated_verses = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)], null=False)
    estimated_words = models.IntegerField(default=1, validators=[MinValueValidator(1)], null=False)
    completed_chapters = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)], null=False)
    completed_verses = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)], null=False)
    completed_words = models.IntegerField(default=1, validators=[MinValueValidator(1)], null=False)


class Chapter(CommonInfo):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_number = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)], null=False)
    estimated_verses = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)], null=False)
    estimated_words = models.IntegerField(default=1, validators=[MinValueValidator(1)], null=False)


class Verse(CommonInfo):
    book = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    verse_number = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)], null=False)
    original_verse = models.CharField(max_length=54, null=False, blank=False)


class VerseCrossReference(CommonInfo):
    original_verse = models.ForeignKey(Verse, related_name='source_verse', on_delete=models.CASCADE)
    reference_verse = models.ForeignKey(Verse, related_name='related_verse', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Verse Cross-Reference")
        verbose_name_plural = _("Verse Cross-References")


class Topic(CommonInfo):
    topic_number = models.IntegerField(default=1, validators=[MinValueValidator(1)], null=False, blank=False)
    topic_title = models.CharField(max_length=12, null=False, blank=False)
    verse_start = models.ForeignKey(Verse, related_name='topic_verse_start', on_delete=models.SET_NULL, null=True)
    verse_end = models.ForeignKey(Verse, related_name='topic_verse_end', on_delete=models.SET_NULL, null=True)
