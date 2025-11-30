from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, AuthorViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='author')

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
