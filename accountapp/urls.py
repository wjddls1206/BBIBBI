from django.urls import path

from accountapp.views import TestView, LogInView

app_name = "accountapp"

urlpatterns = [

    path('', TestView.as_view(), name='test'),
    path('login/', LogInView.as_view(), name='login'),
]