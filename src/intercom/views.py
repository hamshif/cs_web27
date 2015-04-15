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


def webrtc(request):

    response = respond_html(request, "/intercom/static/webrtc/client/html/index.html")

    if settings.WS_TYPE == 'ws':

        response['ssl'] = 'false'

    else:

        response['ssl'] = 'true'


    return response


def roojoom(request):

    response = respond_html(request, "/intercom/static/roojoom/html/index.html")

    if settings.WS_TYPE == 'ws':

        response['ssl'] = 'false'

    else:

        response['ssl'] = 'true'


    return response


def roojoom1(request):

    response = respond_html(request, "/intercom/static/roojoom/html/index1.html")

    if settings.WS_TYPE == 'ws':

        response['ssl'] = 'false'

    else:

        response['ssl'] = 'true'


    return response



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

        "rooms": {
            1:{"num":1, "building":"Rothberg", "wing":"B", "floor":1},
            2:{"num":2, "building":"Rothberg", "wing":"B", "floor":1},
            3:{"num":3, "building":"Rothberg", "wing":"B", "floor":1},
            4:{"num":4, "building":"Rothberg", "wing":"B", "floor":1},
            5:{"num":13, "building":"Rothberg", "wing":"B", "floor":1},
            6:{"num":15, "building":"Rothberg", "wing":"B", "floor":1},
        },

        "personnel": {
            1:{"name":"Danny", "surname":"Braniss", "room":1, "path":"",},
            2:{"name":"Ely", "surname":"Levy", "room":2, "path":"",},
            3:{"name":"Jorge", "surname":"Najenson", "room":3, "path":"",},
            4:{"name":"Raanan", "surname":"Chermoni", "room":4, "path":"",},
            5:{"name":"Tanya", "surname":"Kuzmitski", "room":5, "path":"",},
            6:{"name":"Yair", "surname":"Yarom", "room":5, "path":"",},
            7:{"name":"Chana", "surname":"Slutzkin", "room":5, "path":"",},
            8:{"name":"Dima", "surname":"Surname", "room":4, "path":"",},
            9:{"name":"Tomer", "surname":"Klainer", "room":5, "path":"",},
            10:{"name":"Ephraim", "surname":"Silverberg", "room":6, "path":"",},
            11:{"name":"Pavel", "surname":"Gak", "room":5, "path":"Open Space",},
            12:{"name":"Naama", "surname":"Shemesh", "room":5, "path":"Open Space",},
        },

        "id_order" : [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12],

        "last_update":"the date"
    }

    return d_personnel


@never_cache
def error_report(request):

    """
    """

    response = {"message":"default"}

    try:

        if request.is_ajax():
            if request.method == 'POST':

                j = json.loads(request.body.decode("utf-8"))
                print('error_report: ', j['error_report'])
                # logger.debug('j: ' + j)


        j['message'] = 'followup'
        # logger.debug("j['counter']:" + j['counter'])

        j['text'] = "baff"


    except Exception:

        print(sys.exc_info())
        traceback.print_exc()



    return HttpResponse(json.dumps(response))


@never_cache
def invite_to_room(request):

    """
    """

    response = {"message":"default"}

    try:

        if request.is_ajax():
            if request.method == 'POST':

                j = json.loads(request.body.decode("utf-8"))
                print(str(j))

                print('type(j)', type(j))

                print('room: ', str(j['room']))
                print('browse_text: ', j['personnel']['browse_text'])
                # logger.debug('j: ' + j)

                response['message'] = j['personnel']['browse_text']


    except Exception:

        print(sys.exc_info())
        traceback.print_exc()



    return HttpResponse(json.dumps(response))