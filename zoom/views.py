from django.http.response import JsonResponse
from django.shortcuts import render
import requests
import base64
import json
from django.views.decorators.csrf import csrf_exempt

client_id = "d39KwhSYQaiR7vRsHokOPQ"
client_secret = "EIEKw2nI1vw3JYvemerft7YPDv30zw3m"

def base64Encode(string):
    string_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

def home(request):
    return render(request, 'index.html')


def generate_access_token(request):
    r = requests.post("https://zoom.us/oauth/token?grant_type=authorization_code&code=1zdngydzCT_3YN24D4qTI2pxNAgfgF6dA&redirect_uri=http://127.0.0.1:8000/zoom/callback/", 
    headers= {
        'Authorization': 'Basic' + base64Encode(f'{client_id}:{client_secret}')
        }
    )

    return JsonResponse(r.json())



def get_user_details(request):
    auth_token = request.META.get('HTTP_AUTHORIZATION')
    r = requests.get("https://api.zoom.us/v2/users/me", headers={"Authorization": auth_token})
    return JsonResponse(r.json())

@csrf_exempt
def create_meeting(request):
    auth_token = request.META.get('HTTP_AUTHORIZATION')
    meeting_details = json.loads(request.body)
    print(meeting_details)
    r = requests.post('https://api.zoom.us/v2/users/me/meetings', data= json.dumps(meeting_details), headers={'Authorization': auth_token, 'Content-Type': 'application/json'})
    
    return JsonResponse(r.json())