from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    AuthorViewSet
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = [
    # Book Generic Views
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Author ViewSet via router
    path('', include(router.urls)),
]
