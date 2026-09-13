from django.urls import path
from .views import book_list, book_detail

app_name = 'library'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
]
