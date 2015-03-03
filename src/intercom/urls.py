# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from intercom.views import SocView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = patterns('intercom.views',
    url(r'^intercom/$', 'intercom', name='intercom'),
    url(r'^face_talk/$', 'face_talk', name='face_talk'),
    url(r'^conference/$', 'conference', name='conference'),
    url(r'^serverless_webrtc/$', 'serverless_webrtc', name='serverless_webrtc'),
    url(r'^webrtc_example/$', 'webrtc_example', name='webrtc_example'),

    # url(r'^soc/$', 'soc', name='soc'),


    url(r'^soc/$', SocView.as_view(), name='soc'),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('soc'))),
)

