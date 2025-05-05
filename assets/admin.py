from django.contrib import admin

from assets.forms import LibraryItemForm
from assets.models import LibrarySeller, Library, Category, LibraryItem, LibraryItemLink


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ['name']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


@admin.register(LibrarySeller)
class LibrarySellerAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


# TODO: Setup the "fields" & "fieldsets" properties
@admin.register(LibraryItem)
class LibraryItemAdmin(admin.ModelAdmin):
    form = LibraryItemForm
    empty_value_display = '-empty-'
    fields = [('name', 'category', 'max_ue_version'), ('source_library', 'library_seller'), 'url', ('publish_date',
              'last_updated'), ('license_terms', 'age_rating'), ('promotional_content', 'allows_usage_with_ai',
              'generated_with_ai'), 'description', ('target_android', 'target_gearvr', 'target_hololens2',
              'target_html5', 'target_ios', 'target_linux', 'target_mac', 'target_nintendo_switch', 'target_oculus',
              'target_ps4', 'target_steamvr_htcvive', 'target_win32', 'target_windows', 'target_xboxone'),
              'distribution_method', 'documentation_url']
    list_display = ['name', 'category', 'view_publish_date']
    list_filter = ['category']

    @admin.display(empty_value='???')
    def view_publish_date(self, obj):
        return obj.publish_date.strftime('%B %d, %Y') if obj.publish_date else None
