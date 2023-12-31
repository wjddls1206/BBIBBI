from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, test, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

urlpatterns = [

    path('', test, name='test'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('pill/<int:pk>', AccountDetailView.as_view(), name='pill'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

]