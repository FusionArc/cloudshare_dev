from django.contrib import admin
from django.urls import include, path

from awards.views import award_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('awards/', award_list)
]
