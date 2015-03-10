import json
from django.views.decorators.cache import never_cache
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


@never_cache
def personnel_map(request):

    """
    """

    response = {"message":"default"}

    if request.method == 'GET':

        try:

            g = request.GET

            location = g.__getitem__('location')
            print('location:', location)

        except Exception:

            print('exception: ', sys.exc_info)
            traceback.print_exc()

    return HttpResponse(json.dumps(d_json()))



def d_json():
    """
    """

    d_personnel = {

        "personnel": {
            1:{"name":"Danny", "surname":"Braniss", "room":"B 101", "path":"",},
            2:{"name":"Ely", "surname":"Levy", "room":"B 102", "path":"",},
            3:{"name":"Jorge", "surname":"Najenson", "room":"B 103", "path":"",},
            4:{"name":"Raanan", "surname":"Chermoni", "room":"B 104", "path":"",},
            5:{"name":"Tanya", "surname":"Kuzmitski", "room":"Open Space", "path":"",},
            6:{"name":"Yair", "surname":"Yarom", "room":"Open Space", "path":"",},
            7:{"name":"Chana", "surname":"Slutzkin", "room":"Open Space", "path":"",},
            8:{"name":"Dima", "surname":"Surname", "room":"B 104", "path":"",},
            9:{"name":"Tomer", "surname":"Klainer", "room":"Open Space", "path":"",},
            10:{"name":"Ephraim", "surname":"Silverberg", "room":"Server", "path":"",},
            11:{"name":"Pavel", "surname":"Gak", "room":"Open Space", "path":"Open Space",},
            12:{"name":"Naama", "surname":"Shemesh", "room":"", "path":"Open Space",},
        },

        "id_order" : [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12],

        "update":"the date"
    }

    return d_personnel


