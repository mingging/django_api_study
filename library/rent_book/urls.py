from django.urls import path
from . import views

app_name = 'rent_book'
urlpatterns=[
    path('students/', views.StudentView.as_view()),
    path('students/<int:id>', views.StudentView.as_view()),
    path('book/', views.BookView.as_view()),
    path('book/<int:id>', views.BookView.as_view()),
    path('rent', views.RentView.as_view()),
]