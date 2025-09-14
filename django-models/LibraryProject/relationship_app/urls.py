from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),  # you need to create this view in views.py
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('books/add/', views.add_book, name="add_book/"),
    path('books/edit/<int:book_id>/', views.edit_book, name="edit_book/"),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'), 
]
