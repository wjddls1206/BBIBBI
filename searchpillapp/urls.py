
from django.urls import path

from searchpillapp.views import pills

from django.conf import settings
from django.conf.urls.static import static

app_name = "searchpillapp"

urlpatterns = [

    path('pills/', pills, name='pills'),

]
# media 경로 추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)