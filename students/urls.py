from django.urls import path
from .views import ListCreateStudentView, StudentDetailView, ListCreateCheckPinView, SubjectDetailView, \
    ListCreateSubjectView, ListCreateStudentSubjectView, StudentSubjectDetailView, ListCreateStudentWeightView, \
    StudentWeightDetailView, ListCreateNextTagView, NextTagDetailView

urlpatterns = [
    path('student/', ListCreateStudentView.as_view(), name="Student-list-create"),
    path('check_pin/', ListCreateCheckPinView.as_view(), name="checkpin-list-view"),
    path('student/<int:pk>/', StudentDetailView.as_view(), name="Student-detail"),

    path('subject/', ListCreateSubjectView.as_view(), name="Subject-list-create"),
    path('subject/<int:pk>/', SubjectDetailView.as_view(), name="Subject-detail"),

    path('student-subject/', ListCreateStudentSubjectView.as_view(), name="student-Subject-list-create"),
    path('student-subject/<int:pk>/', StudentSubjectDetailView.as_view(), name="student-subject-detail"),

    path('student-weight/', ListCreateStudentWeightView.as_view(), name="student-weight-list-create"),
    path('student-weight/<int:pk>/', StudentWeightDetailView.as_view(), name="student-weight-detail"),

    path('next_tag/', ListCreateNextTagView.as_view(), name="next-tag-list-create"),
    path('next_tag/<int:pk>/', NextTagDetailView.as_view(), name="next-tag-detail"),
]
