from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_maestros_generales.views import ProvinciasDetail, ProvinciasList, PaisesDetail, PaisesList, MunicipiosDetail, \
    MunicipiosList, TiposTercerosDetail, TiposTercerosList, CodigosPostalesDetail, CodigosPostalesList


__author__ = 'julian'


provincias_urls = patterns('',
    url(r'^/editprovincias/(?P<pk>[0-9]+)$', ProvinciasDetail.as_view(), name='Provincias-detail'),
    url(r'^$', ProvinciasList.as_view(), name='Provincias-list')
)

paises_urls = patterns('',
    url(r'^/editpaises/(?P<pk>[0-9]+)$', PaisesDetail.as_view(), name='Paises-detail'),
    url(r'^$', PaisesList.as_view(), name='Paises-list')
)


municipios_urls = patterns('',
    url(r'^/editmunicipios/(?P<pk>[0-9]+)$', MunicipiosDetail.as_view(), name='Municipios-detail'),
    url(r'^$', MunicipiosList.as_view(), name='Municipios-list')
)

tiposterceros_urls = patterns('',
    url(r'^/edittiposterceros/(?P<pk>[0-9]+)$', TiposTercerosDetail.as_view(), name='TiposTerceros-detail'),
    url(r'^$', TiposTercerosList.as_view(), name='TiposTerceros-list')
)

codigospostales_urls = patterns('',
    url(r'^/editcodigospostales/(?P<pk>[0-9]+)$', CodigosPostalesDetail.as_view(), name='CodigosPostales-detail'),
    url(r'^$', CodigosPostalesList.as_view(), name='CodigosPostales-list')
)


urlpatterns = patterns('',
                       url(r'^provincias', include(provincias_urls)),
                       url(r'^paises', include(paises_urls)),
                       url(r'^municipios', include(municipios_urls)),
                       url(r'^tiposterceros', include(tiposterceros_urls)),
                       url(r'^codigospostales', include(codigospostales_urls)),
                       )


urlpatterns = format_suffix_patterns(urlpatterns)