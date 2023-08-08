from django.urls import path
from .views import ListCreateStudentView, StudentDetailView, ListCreateCheckPinView, SubjectDetailView, \
    ListCreateSubjectView, ListCreateStudentSubjectView, StudentSubjectDetailView, ListCreateStudentWeightView, \
    StudentWeightDetailView, ListCreateNextTagView, NextTagDetailView, ListCreateRecommendationView, \
    ListCreateSubjectWeightView, SubjectWeightDetailView, ListCreateStudentLoginView, StudentResponsesView, \
    StudentRecommendationView

urlpatterns = [
    path('student/', ListCreateStudentView.as_view(), name="Student-list-create"),
    path('login-student/', ListCreateStudentLoginView.as_view(), name="Student-list-login-create"),
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

    path('save_quizes/', ListCreateRecommendationView.as_view(), name="recommendation-list-create"),
    path('student_recommendations/<int:pk>/', StudentRecommendationView.as_view(), name="student-recommendations"),
    path('student_responses/<int:pk>/', StudentResponsesView.as_view(), name="student-responses"),

    path('subject-weights/', ListCreateSubjectWeightView.as_view(), name="subject-weights-list-create"),
    path('subject-weights/<int:pk>/', SubjectWeightDetailView.as_view(), name="subject-weight-detail")
]
