from django.contrib import admin

from kjvhb.models import Author


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass