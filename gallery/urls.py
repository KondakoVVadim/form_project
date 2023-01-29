from django.urls import path
from .views import CreateGalleryView, ListGallery
urlpatterns = [
    path('load_image', CreateGalleryView.as_view()),
    path('list_image', ListGallery.as_view())
]