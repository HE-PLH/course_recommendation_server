from django.urls import path
from .views import ListCreateStudentView, StudentDetailView,ListCreateCheckPinView

urlpatterns = [
    path('student/', ListCreateStudentView.as_view(), name="Student-list-create"),
    path('check_pin/', ListCreateCheckPinView.as_view(), name="checkpin-list-view"),
    path('student/<int:pk>/', StudentDetailView.as_view(), name="Student-detail"),
]
