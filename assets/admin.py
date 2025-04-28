from django.contrib import admin

from assets.models import LibrarySeller, Library, Category, LibraryItem, LibraryItemLink


# Register your models here.
class AdditionalLinkInline(admin.TabularInline):
    model = LibraryItemLink
    extra = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass


@admin.register(LibrarySeller)
class LibrarySellerAdmin(admin.ModelAdmin):
    pass


@admin.register(LibraryItem)
class LibraryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    inlines = [AdditionalLinkInline]

