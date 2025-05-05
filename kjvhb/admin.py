from django.contrib import admin

from kjvhb.models import Author, Book, Chapter, Verse, Topic, VerseCrossReference


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass


@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(VerseCrossReference)
class VerseCrossReferenceAdmin(admin.ModelAdmin):
    pass
