
from django.urls import path

from pharmacyapp.views import pharmacy

app_name = "pharmacyapp"

urlpatterns = [

    path('pharmacy/', pharmacy, name='pharmacy'),

]