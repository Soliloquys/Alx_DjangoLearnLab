from django.urls import path
from .views import list_books, register_view
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Task 2 URLs
    path('books/', list_books, name='list_books'),                       # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV

    # Task 3 URLs
    path('register/', register_view, name='register'),                   # function-based
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),    # class-based
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), # class-based
]
