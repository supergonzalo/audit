from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^audit/', include('audit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^lista/$', 'scorecard.views.lista'),
    (r'^lista/edificio/(.*)', 'scorecard.views.edif'),
    (r'^head', 'scorecard.views.formato'),
    (r'^$', 'scorecard.views.home'),

)

