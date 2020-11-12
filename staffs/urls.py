from django.urls import path

from .views import StaffListView, StaffDetailView, StaffUpdateView

urlpatterns = [
    path('list/', StaffListView.as_view(), name='staff-list'),
    path('<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('<int:pk>/update/', StaffUpdateView.as_view(), name='staff-update'),
   
]
