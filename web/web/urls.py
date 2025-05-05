
from django.contrib import admin
from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Root URL
    path('index/', views.index, name='index'),
    path('reg/', views.reg, name='reg'),
    path('sav/', views.sav, name='sav'),
    path('home/', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('jobview/', views.jobview, name='jobview'),
    path('nontech/', views.nontech, name='nontech'),
    path('applyform/', views.applyform, name='applyform'),
    path('success/', views.success, name='success'),
    path('signout/', views.signout, name='signout'),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)