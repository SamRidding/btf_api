from django.urls import path
from mixes import  views


urlpatterns = [
    path('mixes/', views.MixList.as_view()),
    path('mixes/<int:pk>/', views.MixDetail.as_view())
]
