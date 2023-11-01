from django.urls import path

from accountapp.views import TestView

app_name = "accountapp"

urlpatterns = [

    path('test/', TestView.as_view(), name='test'),

]