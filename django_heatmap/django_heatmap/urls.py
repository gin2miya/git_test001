from django.contrib import admin

from django.urls import include, path

urlpatterns = [

    path('maps/', include('maps.urls')),

    path('admin/', admin.site.urls),
]
