import requests
import urllib
from http.cookies import SimpleCookie
from http.cookiejar import Cookie, CookieJar 
import datetime
import json
from collections import namedtuple

cookie = {}
url = 'https://www.kroger.com'
signin = '/signin'
authenticate = '/user/authenticate'
favorites = '/storecatalog/clicklistbeta/api/items/personalized/myFavorites'
ecommercesetupurl = '/onlineshopping'
storesetup = '/storecatalog/servlet/OnlineShoppingStoreSetup'
nextbasket = '/products/api/next-basket'
toggles = '/basket/api/toggles'
logon = '/storecatalog/servlet/Logon'
firstname = '/profile/getFirstNameFromSession'
getauthstate = '/user/getAuthenticationState'
pickstore = '/account/pickStore'
profile = '/accountmanagement/api/profile'
stores = '/stores'
addToCart = '/storecatalog/clicklistbeta/api/cart/item'
cart = '/storecatalog/clicklistbeta/api/cart'
items = '/storecatalog/clicklistbeta/api/items/upc/'

class cart():
    def __init__():
        self.basketId = 0
        self.cartItems = []
        self.count = 0
        self.duplicateItemRemoved = False
        self.index = 0
        self.orderId = 0
        self.serviceFee = 0
        self.serviceFeeDiscount    = 0     
        self.subtotal = 0.0
        self.total = 0.0

def encode(cookie):
    encodedcookie = ''
    for key, value in cookie.items():
        encodedcookie = encodedcookie + key + '=' + value + ';'
    return encodedcookie

def updatecookie(cookie, setcookietext):
    setcookietext = setcookietext.replace('ecure,', 'ecure;')
    setcookietext = setcookietext.replace('nly,', 'nly;')
    setcookie = SimpleCookie()
    setcookie.load(rawdata = setcookietext)
    for key, morsel in setcookie.items():
        cookie[key] = morsel.value        
    return cookie

def printcookie(cookie):
    for key, morsel in sorted(cookie.items()):
        print(key, ": ", morsel)

header = {
    'host': "www.kroger.com",
    'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0",
    'accept': "application/json, text/plain, */*",
    'accept-language': "en-US,en;q=0.5",
    'accept-encoding': "gzip, deflate, br",
    'referer': "https://www.kroger.com/signin?redirectUrl=/",
    'content-type': "application/json;charset=utf-8",
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'X-XSRF-TOKEN': "",
    }

session = requests.Session()
session.headers.update(header)
#This is where I get the XSRF token initially.  May not be necessary.
session.get(url + nextbasket)
session.headers.update({'X-XSRF-TOKEN':session.cookies['XSRF-TOKEN']})
#This is where I authenticate and get my store information
payload = "{\"account\":{\"email\":\"johns10davenport@gmail.com\",\"password\":\"A7B!2#x2y\",\"rememberMe\":null},\"location\":\"\"}"
response = session.post(url + authenticate, data=payload)
#This is where I update the store information cookies based on data I return from the authentication workflow.
session.cookies.set_cookie(Cookie(version=0, name='StoreLocalName', value=response.json()['store']['storeInformation']['localName'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
session.cookies.set_cookie(Cookie(version=0, name='StoreCode', value=response.json()['store']['storeInformation']['localName'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
session.cookies.set_cookie(Cookie(version=0, name='StoreAddress', value=(response.json()['store']['storeInformation']['address']['addressLineOne'].replace(' ', '+') + ",+" + response.json()['store']['storeInformation']['address']['city'].replace(' ', '+') + ",+" + response.json()['store']['storeInformation']['address']['state'].replace(' ', '+')), port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
session.cookies.set_cookie(Cookie(version=0, name='StoreInformation', value=(response.json()['store']['storeInformation']['address']['addressLineOne'].replace(' ', '+') + ",+" + response.json()['store']['storeInformation']['address']['city'].replace(' ', '+') + ",+" + response.json()['store']['storeInformation']['address']['state'].replace(' ', '+')+response.json()['store']['storeInformation']['phoneNumber'] + "," + response.json()['store']['pharmacyInformation']['phoneNumber']), port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
session.cookies.set_cookie(Cookie(version=0, name='StoreZipCode', value=response.json()['store']['storeInformation']['address']['zipCode'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))

session.get(url + nextbasket)
session.get(url + toggles)
zip = session.get(url + profile).json()['address']['zip']
payload = {'address': str(zip),'maxResults':'5','radius':'300','storeFilters':'94'}
stores = session.get(url + stores, params=payload)
storeIndex = 0

session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStoreDivision', value=stores.json()[storeIndex]['storeInformation']['divisionNumber'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStore', value=stores.json()[storeIndex]['storeInformation']['storeNumber'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStoreStreetAddress', value=stores.json()[storeIndex]['storeInformation']['address']['addressLineOne'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStoreCity', value=stores.json()[storeIndex]['storeInformation']['address']['city'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStoreZipCode', value=stores.json()[storeIndex]['storeInformation']['address']['zipCode'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))

session.get(url + storesetup) #Adds WC_Persistent
payload = "{\"divisionNumber\":\"024\",\"storeNumber\":\"00339\",\"storeType\":\"pick\"}"
session.post(url + pickstore, data=payload)
payload = {'pickupStoreId': '02400753', 'divisionSwitch': 'true', 'catalogId': '11051', 'langId': '', 'storeId': '11151', 'URL': 'https://www.kroger.com/storecatalog/servlet/TopCategoriesDisplayView?storeId=11151&catalogId=11051&langId=-1'}
session.get(url + logon, params=payload)

#Everything is complete.  Check that we can get the favorites data.
session.get(url + favorites)

#Pull the contents of the cart and print the JSON
cartresponse = session.get(url + cart)
cart = json.loads(cartresponse.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print(cart)

#Grab an item from the api by UPC code
upc = '0001111050268'
for item in cart.cartItems:
    print(dir(item))
    print(item.productId)

    
    
    
upcitem = session.get(url + items + upc)
x = json.loads(upcitem.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


#Now post 

print(x.name)

session.get('https://www.kroger.com/storecatalog/clicklistbeta/clearWCSCookies')


session.get('https://www.kroger.com/storecatalog/servlet/Logon?pickupStoreId=02400339&divisionSwitch=true&catalogId=11051&langId=&storeId=11151')

for item in session.cookies:
    print(item.version)
    print(item.name)
    print(item.value)
    print(item.port)
    print(item.port_specified)
    print(item.domain)
    print(item.domain_specified)
    print(item.secure)
    print(item.expires)
    print(item.expires)
    print(type(item.expires))
    print(item.discard)
    #print(dir(item))

for item in session.cookies:
    print(item)
    
for item in response.cookies:
    print(item)

for item in response.history:
    for cookie in item.cookies.get_dict().items():
        print(cookie)
    
session.headers.update(session.get(url + nextbasket, headers=header).)

cookie = updatecookie(cookie, response.headers['set-cookie'])
#encodedcookie = encode(cookie)
#header['cookie'] = encodedcookie
header['X-XSRF-TOKEN'] = cookie['XSRF-TOKEN']
#printcookie(cookie)
print(response)
#Authenticate
cookie = updatecookie(cookie, response.headers['set-cookie'])
#encodedcookie =  encode(cookie)
#header['cookie'] = encodedcookie
print(response)
header['X-XSRF-TOKEN'] = cookie['XSRF-TOKEN']
#printcookie(cookie)
responsejson = response.json()
#Next-Basket
response = requests.request("GET", url + nextbasket, headers=header, cookies = cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])
#encodedcookie =  encode(cookie)
#header['cookie'] = encodedcookie
print(response)
header['X-XSRF-TOKEN'] = cookie['XSRF-TOKEN']
#printcookie(cookie)
response = requests.request("GET", url + toggles, headers=header, cookies = cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])
#encodedcookie =  encode(cookie)
#header['cookie'] = encodedcookie
print(response)
header['X-XSRF-TOKEN'] = cookie['XSRF-TOKEN']
#printcookie(cookie)
#Online Shopping Setup
#encodedcookie =  encode(cookie)
#header['cookie'] = encodedcookie
sacv(cookie)
print(response)
header['X-XSRF-TOKEN'] = cookie['XSRF-TOKEN']
response = requests.request("GET", url + storesetup, headers=header, cookies = cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])
#encodedcookie =  encode(cookie)
#header['cookie'] = encodedcookie
print(response)
header['X-XSRF-TOKEN'] = cookie['XSRF-TOKEN']
#printcookie(cookie)
response = requests.request("GET", 'https://www.kroger.com/storecatalog/servlet/Logon?pickupStoreId=02400339&divisionSwitch=true&catalogId=11051&langId=&storeId=11151&URL=https://www.kroger.com/storecatalog/servlet/TopCategoriesDisplayView?storeId=11151&catalogId=11051&langId=-1', headers = header, cookies = cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])
#encodedcookie =  encode(cookie)
#header['cookie'] = encodedcookie
print(response)
header['X-XSRF-TOKEN'] = cookie['XSRF-TOKEN']
printcookie(cookie)

