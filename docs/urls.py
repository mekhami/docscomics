from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'docs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name="index"),
)
