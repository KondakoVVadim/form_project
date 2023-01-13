from django.urls import path
from .views import Done, FeedBackView, UpdateView
urlpatterns = [
    path('', FeedBackView.as_view()),
    path('done/', Done.as_view()),
    path('<int:id_feedback>', UpdateView.as_view())
]