from django.urls import path
from . import views
from .views import StaffListView, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDetailView, StaffDeleteView
from .views import student_list, StudentDeleteView, StudentDetailView, StudentUpdateView, StudentCreateView

urlpatterns = [
    path('register/', views.registerPage, name="register"),
   	path('login/', views.loginPage, name="login"),
   	path('logout/', views.logoutUser, name="logout"),

    path('list', student_list, name='student-list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),

    path('list/', StaffListView.as_view(), name='staff-list'),
    path('<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('create/', StaffCreateView.as_view(), name='staff-create'),
    path('<int:pk>/update/', StaffUpdateView.as_view(), name='staff-update'),
    path('<int:pk>/delete/', StaffDeleteView.as_view(), name='staff-delete'),
]

