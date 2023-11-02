from django.urls import path

from accountapp.views import TestView

app_name = "accountapp"

urlpatterns = [

    path('', TestView.as_view(), name='test'),

]