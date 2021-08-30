from django.contrib import admin
from django.urls.conf import include, path
from django.conf.urls import url

from mainapp.views import MainPageView

urlpatterns = [
    # path('', MainPage/View.as_view(), name='home'),
    # url(r'^admin/', admin.site.urls),
    # url(r'','mainapp.views.main'),
    
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls'))
]
