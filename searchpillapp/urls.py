
from django.urls import path

from searchpillapp.views import pills

app_name = "searchpillapp"

urlpatterns = [

    path('pills/', pills, name='pills'),

]