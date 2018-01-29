from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reaction/(?P<reaction_id>\w+)/$', views.reaction_test_page, name='reaction_test_page')
]
