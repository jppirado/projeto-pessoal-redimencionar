from django.urls import path

from .views import IndexView , SuccessPageView

urlpatterns = [
    path('' , IndexView.as_view(), name='index'),
    path('success/' , SuccessPageView.as_view() , name='successurl')
]