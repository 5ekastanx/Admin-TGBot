from django.urls import path
from .views import (
    NotesListCreateView,
    NotesDetailView,
    CreateUserView,
    UserDetail,
    UserList
)

urlpatterns = [
    path('notes/', NotesListCreateView.as_view(), name='notes-detail'),
    path('notes/<int:pk>/', NotesDetailView.as_view(), name='notes-detail'),
    path('register/', CreateUserView.as_view(), name='create_user'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetail.as_view(), name='user-detail'),
]
