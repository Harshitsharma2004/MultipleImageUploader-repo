from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_image, name='upload'),
    path('view/', views.view_images, name='view_images'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
