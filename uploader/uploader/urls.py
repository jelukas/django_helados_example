from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #    url(r'^$',TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^$','gestor.views.listar_helados', name='home'),
    # url(r'^uploader/', include('uploader.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^admin/', include(admin.site.urls)),

)


#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,show_indexes=False)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)