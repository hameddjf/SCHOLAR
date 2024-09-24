from django.views.generic import View
from django.http import HttpResponse

from .models import Category, Tag


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return HttpResponse(', '.join([category.name for category in categories]))


class CategoryDetailView(View):
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            return HttpResponse(f"Category: {category.name}")
        except Category.DoesNotExist:
            return HttpResponse("Category not found", status=404)


class TagListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return HttpResponse(', '.join([tag.name for tag in tags]))


class TagDetailView(View):
    def get(self, request, slug):
        try:
            tag = Tag.objects.get(slug=slug)
            return HttpResponse(f"Tag: {tag.name}")
        except Tag.DoesNotExist:
            return HttpResponse("Tag not found", status=404)
