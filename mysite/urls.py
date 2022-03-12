
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('job1app.urls')),
    path('accounts/', include('users.urls')),
    path('contact', include('contact.urls')),
    path('subscriber/', include('subscriber.urls')),
    # path('accounts/', include('allauth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
