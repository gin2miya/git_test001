from django.urls import path

from . import views

from django.conf import settings #追加   
from django.conf.urls.static import static #追加

urlpatterns = [

    path('', views.index, name='index'),

    path('calc', views.calc),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #追加
