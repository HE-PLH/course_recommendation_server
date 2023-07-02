from django.urls import path
from .views import ListCreateChatsView, ChatsDetailView, TagsDetailView, ListCreateTagsView, ListCreatePatternsView, \
    PatternsDetailView, ResponsesDetailView, ListCreateResponsesView, ListCreateTrainingDataView, \
    TrainingDataDetailView, ListCreateAskView

urlpatterns = [
    path('ask/', ListCreateAskView.as_view(), name="Ask"),

    path('chats/', ListCreateChatsView.as_view(), name="Chats-list-create"),
    path('tags/', ListCreateTagsView.as_view(), name="tags-list-create"),
    path('patterns/', ListCreatePatternsView.as_view(), name="pattern-list-create"),
    path('responses/', ListCreateResponsesView.as_view(), name="responses-list-create"),

    path('get-training-data/', ListCreateTrainingDataView.as_view(), name="get-training-data"),

    path('chats/<int:pk>/', ChatsDetailView.as_view(), name="Chats-detail"),
    path('tags/<int:pk>/', TagsDetailView.as_view(), name="Tags-detail"),
    path('patterns/<int:pk>/', PatternsDetailView.as_view(), name="Patterns-detail"),
    path('responses/<int:pk>/', ResponsesDetailView.as_view(), name="Responses-detail"),

    path('get-training-data/<int:pk>/', TrainingDataDetailView.as_view(), name="Training-Data-detail")
]
