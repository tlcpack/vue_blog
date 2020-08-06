from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('seasons/', views.SeasonList.as_view()),
    path('seasons/<int:pk>', views.SeasonDetail.as_view()),
]
