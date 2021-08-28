from django.contrib import admin
from django.urls.conf import include, path

from mainapp.views import MainPageListView

urlpatterns = [
    path('', MainPageListView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    path('main/', include('mainapp.urls'))
]
