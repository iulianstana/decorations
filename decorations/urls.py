from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from frontend.views import IndexView, CategoryView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^category/(?P<cat_id>\d+)', CategoryView.as_view(), name='category'),

    url(r'^admin/', include(admin.site.urls)),
)
