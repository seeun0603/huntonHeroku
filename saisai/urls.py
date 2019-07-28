
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main'),
    path('board/', include('board.urls')),
    path('login/', include('login.urls'), name='login'),
    path('signup/', include('signup.urls'), name= 'signup'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
