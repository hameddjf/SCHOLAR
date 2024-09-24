from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Tag


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'slug')
    list_display_links = ('indented_title',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    def get_prepopulated_fields(self, request, obj=None):
        return self.prepopulated_fields


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
