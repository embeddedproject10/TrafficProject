from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   # url(r'^users/(?P<place_name_input>\w{0,50})/(?P<crowded_input>\w{0,5})/$', 'myapp.views.is_Crowded'),
)
