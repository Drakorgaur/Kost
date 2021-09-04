from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from django.urls import include
from django.conf.urls import include, url
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('main.urls')),
    path('chat/', include('chat.urls')),
    path('mafia/', include('mafia.urls')),
    path('', RedirectView.as_view(url='/index/', permanent=True)),
    #url(r'^account/', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
