import django
from puretacodiet.models import *
from django.db.models import Count, Avg

planinstances = PlanInstance.objects.all()
for planinstance in planinstances:
    print(planinstance.date)
    for meal in planinstance.plan.meals.all():
        for recipe in meal.recipes.all():
            for ingredient in recipe.ingredients.all():
                recipeingredient = RecipeIngredient.objects.get(ingredient=ingredient,recipe=recipe)
                print(recipeingredient.quantity)
                print(ingredient.title)
                print(ingredient.uom)
                                
planinstance = PlanInstance.objects.get(pk=2)

recipe = Recipe.objects.get(pk=3)
for ingredient in recipe.ingredients.all():
    print(ingredient.title)

list = Ingredient.objects.filter(recipe__meal__plan__planinstance__date__gte = "2017-08-27").filter(recipe__meal__plan__planinstance__date__lte = "2017-09-02")
for item in list:
    print(item.title)
    print(item.uom)
    
meallist = Recipe.objects.filter(meal__plan__planinstance__date__gte = "2017-08-27").filter(meal__plan__planinstance__date__gte = "2017-09-02")

meallist = Recipe.objects.values('pk').values('title').annotate(count=sum('title')).filter(meal__plan__planinstance__date__gte = "2018-08-28", meal__plan__planinstance__date__lte = "2018-09-02")

#This query gets a list of ingredients and quantities from a date range
meallist = MealItem.objects.filter(meal__plan__planinstance__date__gte = "2018-08-28", meal__plan__planinstance__date__lte = "2018-09-02").values('recipe').annotate(total_quantity = Sum('quantity'))
meallist

list = Ingredient.objects.filter(recipe__meal__plan__planinstance__date__gte = "2018-08-28", recipe__meal__plan__planinstance__date__lte = "2018-09-02").values('pk').values('uom').annotate(meal_quantity = Sum('recipe__meal__mealitem__quantity'))
list

list = Ingredient.objects.filter(recipe__meal__plan__planinstance__date__gte = "2018-08-28", recipe__meal__plan__planinstance__date__lte = "2018-09-02").values('pk', 'title', 'uom', 'recipeingredient__quantity').annotate(meal_quantity = Sum('recipe__meal__mealitem__quantity'))
list

#Here is a basic Kroger Clicklist API call


def login(email, password): 
body = {
    "account": {
        "email": email,
        "password": password,
        "rememberMe": True
    },
    "location": ''
}



api._jar = request.jar();

return post(urls.authenticate, body)
    .then(createCookies)
    .then(setupOnlineShopping)
    .then(logEnd('login'))
    .catch(logAndThrow('login'));

function createCookies(resp) {
    createStoreCookies(api._jar, resp.store.storeInformation);
    return resp;

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import requests
import ssl

email = 'johns10davenport@gmail.com'
password = 'A7B!2#x2y'
base = 'https://www.kroger.com'
authenticate = '/user/authenticate'
favorites = '/storecatalog/clicklistbeta/api/items/personalized/myFavorites'
recentPurchases = '/storecatalog/clicklistbeta/api/items/personalized/recentPurchases/quick'

class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLSv1)

params = {
    "account": {
        "email": email,
        "password": password,
        "rememberMe": True
    },
    "location": ''
}

    #'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0;… Gecko/20100101 Firefox/54.0',
    #'Cookie' : 'DSLV=Fri%20Aug%2025%202017%20…ubmVyfDF8U2hvcHBpbmdMaXN0fDE',
    
headers = {
    'Host' : 'www.kroger.com',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Referer' : 'https://www.kroger.com/signin?redirectUrl=/',
    'Content-Type' : 'application/json;charset=utf-8',
    'x-correlation-id' : '8dcec321-5f1f-4264-88be-646085bd5436-1503702303354-11',
    'X-XSRF-TOKEN' : 'da589fac-958e-4707-8a4d-81ab62da709d',
    'Content-Length' : '105',
    'Connection' : 'keep-alive'
}

from urllib3 import HTTPConnectionPool
pool = HTTPConnectionPool(host='www.kroger.com',port=443, maxsize=1, headers=headers)
r = pool.request(method='POST', url='/user/authenticate', headers=headers, params=params)

import requests
r = requests.get('https://www.google.com')












url=base+authenticate
s = requests.Session()
s.mount('https://', MyAdapter())
r=s.post(url,json=params,headers=headers)
html=r.text
print html


response = requests.post(url, params=params, headers=headers)


import ssl
import socket
HOST, PORT = 'www.kroger.com', 443
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
wrappedSocket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ALL")
wrappedSocket.connect((HOST, PORT))

import ssl
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
r = http.request('POST', 'https://www.kroger.com')
r.status
r.data

from urllib3 import HTTPConnectionPool
pool = HTTPConnectionPool(host='www.kroger.com',port=443, maxsize=1, headers=headers)
r = pool.request(method='POST', url='/user/authenticate', headers=headers, params=params)
r.status
r.headers['content-type']
len(r.data) # Content of the response
r = pool.request('POST', '/ajax/services/search/web', fields={'q': 'python', 'v': '1.0'})
len(r.data) # Content of the response
pool.num_connections
pool.num_requests

import urllib3
import logging
from http.client import HTTPConnection
HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
http = urllib3.PoolManager()
r = http.request('GET', 'http://www.kroger.com/storecatalog/clicklistbeta/api/items/personalized/myFavorites')
r.status
r.data

import requests
s = requests.Session()
r = s.get('https://www.kroger.com')
print(r.text)

import urllib3
url = "https://www.google.com" 
r = urllib2.urlopen(url)
print r.read()

import urllib.request
with urllib.request.urlopen('https://www.google.com/') as response:
   html = response.read()
   
import urllib.parse
import urllib.request

url = 'https://www.kroger.com'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   
