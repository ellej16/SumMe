from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'summe_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'summe_app.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summe', 'summe_app.views.index'),
    url(r'^uploadFile', 'summe_app.views.uploadFile')

)
