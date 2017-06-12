from django.conf.urls import url
from nerflix import views

urlpatterns = [
    url(r'^$', views.movie_list, name='movie_list'),
    url(r'^new$', views.movie_create, name='movie_create'),
    url(r'^edit/(?P<pk>\d+)$', views.movie_update, name='movie_edit'),
]
