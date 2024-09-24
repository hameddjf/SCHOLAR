from django.urls import path
from . import views

app_name = 'tags'

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/',
         views.CategoryDetailView.as_view(), name='category_detail'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tags/<slug:slug>/', views.TagDetailView.as_view(), name='tag_detail'),
]
