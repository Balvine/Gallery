from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # landing page
    url('^$', views.photos, name='photos'),
]