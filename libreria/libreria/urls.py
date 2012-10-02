from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from main import views
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', views.index),
    (r'^books/$', views.booksView),
    (r'^book/$', views.book_manageView),
    (r'^book/(?P<id>\d+)/', views.book_manageView),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #imagenes
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
    # Examples:
    # url(r'^$', 'libreria.views.home', name='home'),
    # url(r'^libreria/', include('libreria.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
