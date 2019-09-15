from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submission/<int:submission_id>/upvote/',
         views.upvote,
         name='upvote'),
    path('submission/create/',
         views.create,
         name='create'),
]
