from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
                       url(regex=r'^ex1/$',
                           view=TemplateView.as_view(
                               template_name='ex1/index.html')
                           ),

                       url(regex=r'^ex2/$', view='ex2.views.index'),

                       url(regex='^accounts/',
                           view=include('django.contrib.auth.urls')),

                       url(regex=r'^accounts/logout_login/$',
                           view='django.contrib.auth.views.logout_then_login'),

                       url(regex=r'^ex2/sort/$',
                           view='ex2.views.sort_view'),
                       )
