from django.urls import path
from .views import DoneView, FeedBackView, UpdateView, ListFeedBack, DetailFeedBack, FeedBackViewUpdate
urlpatterns = [
    path('', FeedBackView.as_view()),
    path('done/', DoneView.as_view()),
    path('<int:id_feedback>', UpdateView.as_view()),
    path('list', ListFeedBack.as_view(), name='list'),
    path('detail/<int:pk>', DetailFeedBack.as_view(), name='user_id'),
    path('update/<int:pk>', FeedBackViewUpdate.as_view())
]