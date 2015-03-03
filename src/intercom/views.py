import os
import traceback
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
import sys
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from cs_web27 import settings
from django.core.context_processors import csrf

# Create your views here.

from cs_res27.util import respond_html

def intercom(request):

    return respond_html(request, "/intercom/templates/intercom/index.html")


def face_talk(request):

    return respond_html(request, "/intercom/templates/intercom/face_talk.html")


def conference(request):

    return respond_html(request, "/intercom/templates/intercom/ind1.html")


def serverless_webrtc(request):

    return respond_html(request, "/intercom/templates/intercom/serverless-webrtc.html")


def webrtc_example(request):

    return respond_html(request, "/intercom/templates/intercom/webrtc_example.html")


def soc(request):

    return respond_html(request, "/intercom/templates/intercom/soc.html")





class SocView(TemplateView):

    template_name = 'soc.html'

    facility = 'foobar'

    def get(self, request, *args, **kwargs):
        welcome = RedisMessage('Hello you sniveling fools')  # create a welcome message to be sent to everybody
        RedisPublisher(facility='foobar', broadcast=True).publish_message(welcome)
        return super(SocView, self).get(request, *args, **kwargs)