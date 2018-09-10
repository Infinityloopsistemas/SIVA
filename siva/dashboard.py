# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name
from django.contrib.auth.models import Group

from siva import settings


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        self.children.append(modules.AppList(
            _('Lista: Applicaciones'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))
        
        self.children.append(modules.ModelList(
            _('Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))
        

        grupos_user = context.get('user').groups.all()
        grupo_admin = Group.objects.get(name="administradores")
        grupo_vet = Group.objects.get(name="veterinarios")
        if grupo_admin in grupos_user:
            self.children.append(modules.LinkList(_('Gestión Usuarios'),
                                                  column=2,
                                                  children=[
                                                            {
                                                             'title': _('Crear multiples usuarios'),
                                                             'url':"%sgestion_usuarios/crear_usuarios/" % (settings.URL_SERVER),
                                                             'external': True,
                                                             },
                                                            {
                                                             'title': _('Crear usuario'),
                                                             'url':"%sgestion_usuarios/crear_usuario/" % (settings.URL_SERVER),
                                                             'external': True,
                                                             },
                                                            {
                                                             'title': _('Borrar multiples usuarios'),
                                                             'url':"%sgestion_usuarios/borrar_usuarios/" % (settings.URL_SERVER),
                                                             'external': True,
                                                             },
                                                            {
                                                             'title': _('Borrar usuario'),
                                                             'url':"%sgestion_usuarios/borrar_usuario/" % (settings.URL_SERVER),
                                                             'external': True,
                                                             },
                                                            {
                                                             'title': _('Modificar usuarios'),
                                                             'url':"%sgestion_usuarios/modificar_usuario/" % (settings.URL_SERVER),
                                                             'external': True,
                                                             },
                                                            {
                                                             'title': _('Comprobar usuarios empresas'),
                                                             'url':"%sgestion_usuarios/comprobar_usuarios_empresas/" % (settings.URL_SERVER),
                                                             'external': True,
                                                             },
                                                            

                                                    ]
                                                  ))
        
        if grupo_vet in grupos_user:
            self.children.append(modules.LinkList(_('Gestión Usuarios'),
                                                  column=2,
                                                  children=[                                                            
                                                            {
                                                             'title': _('Modificar usuarios'),
                                                             'url':"%sgestion_usuarios/modificar_usuario/" % (settings.URL_SERVER),
                                                             'external': True,
                                                             },
                                                    ]
                                                  ))
        self.children.append(modules.LinkList(
            _('Soporte'),
            column=2,
            children=[
                {
                    'title': _('Soporte InfinityLoop Sistemas'),
                    'url': 'http://www.infinityloop.es/helpdesk',
                    'external': True,
                },

            ]
        ))
        
      

        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


