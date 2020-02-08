from django.urls import path
from speech import views

urlpatterns = [
    path('speech/', views.RequestItemList.as_view()),
]