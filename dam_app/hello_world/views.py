from asyncio.log import logger
from logging import DEBUG, WARNING, log
import re
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from hello_world.models import User
from django.core.serializers import serialize
import json

# Maps
import folium
import geemap.foliumap as geemap

# Create your views here.

@require_http_methods(["GET"])
def test_view(request):
  log(level=DEBUG, msg="Test Log")
  return http.HttpResponse("Hello World", content_type="text/plain")

@require_http_methods(["POST", "GET"])
def create_user(request):
  log(level=DEBUG, msg="Create User!")
  
  user = User()
  user.first_name = "John"
  user.last_name = "Smith"
  
  user.save()
  
  response = http.HttpResponse(user, content_type="text/plain")
  response.status_code = 201
    
  return response

@require_http_methods(["GET"])
def get_user(request, id):
  log(level=DEBUG, msg="Get User!")
  
  user = User.objects.get(id=id)
  
  response = http.HttpResponse(serialize("json", [user], fields=('first_name', 'last_name')), content_type="text/json")
  response.status_code = 200
    
  return response

@require_http_methods(["GET"])
def home(request):
  figure = folium.Figure()

  Map = geemap.Map(plugin_Draw = True, 
                    Draw_export = True)

  Map.add_to(figure)

  Map.setOptions('SATELLITE');
  
  figure.render()
  
  return render(request, "home.html", {
    "app_name": "Hello, World!",
    "map": figure
  })
  
template_name = 'map.html'


@require_http_methods(["POST", "GET"])
def processCoords(request):
  body = request.body.decode('utf-8')
  
  log(level=WARNING, msg=body)
  data = json.loads(body)
  response = http.JsonResponse(data, content_type="text/json")
  response.status_code = 200
  
  return response
