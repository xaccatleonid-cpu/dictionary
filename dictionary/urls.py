from django.urls import path
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.home, name='home'),
    path('language/add/', views.add_language, name='add_language'),
    path('language/<int:pk>/', views.language_detail, name='language_detail'),
    path('language/<int:pk>/edit/', views.edit_language, name='edit_language'),
    path('language/<int:pk>/delete/', views.confirm_delete_language, name='delete_language'),
    path('language/<int:pk>/word/add/', views.add_word, name='add_word'),
    path('word/<int:pk>/edit/', views.edit_word, name='edit_word'),
    path('word/<int:pk>/delete/', views.confirm_delete_word, name='delete_word'),
]
