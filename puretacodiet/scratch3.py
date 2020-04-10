import requests
import urllib
from http.cookies import SimpleCookie

cookie = {}
url = 'https://www.kroger.com'
signin = '/signin'
authenticate = '/user/authenticate'
favorites = '/storecatalog/clicklistbeta/api/items/personalized/myFavorites'
ecommercesetupurl = '/onlineshopping'
storesetup = '/storecatalog/servlet/OnlineShoppingStoreSetup'
nextbasket = '/products/api/next-basket'
toggles = '/basket/api/toggles'
logon = '/servlet/logon'
firstname = '/profile/getFirstNameFromSession'
getauthstate = '/user/getAuthenticationState'

def encode(cookie):
    encodedcookie = ''
    for key, value in cookie.items():
        encodedcookie = encodedcookie + key + '=' + value + ';'
    return encodedcookie

def printcookies(cookie):
    encodecookie = ''
    for key, value in cookie.items():
        print(key, ': ', value)

def updatecookie(cookie, setcookietext):
    setcookietext = setcookietext.replace('ecure,', 'ecure;')
    setcookietext = setcookietext.replace('nly,', 'nly;')
    setcookie = SimpleCookie()
    setcookie.load(rawdata = setcookietext)
    for key, morsel in setcookie.items():
        cookie[key] = morsel.value        
    return cookie, setcookie

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

#Toggles, whatever that is
response = requests.request("GET", url + toggles, headers=header, cookies = cookie)
setcookie, cookie = updatecookie(cookie, response.headers['set-cookie'])
response = requests.request("GET", url + firstname, headers=header, cookies = cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])
response = requests.request("GET", url + getauthstate, headers=header, cookies = cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])
response = requests.request("GET", url + toggles, headers=header, cookies = cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])
#Pre-Authentication
response = requests.request("GET", url + nextbasket, headers=header)
cookie = updatecookie(cookie, response.headers['set-cookie'])
header['X-XSRF-TOKEN'] = cookie['XSRF-TOKEN']
#Authentication
payload = "{\"account\":{\"email\":\"johns10davenport@gmail.com\",\"password\":\"A7B!2#x2y\",\"rememberMe\":null},\"location\":\"\"}"
response = requests.request("POST", url + authenticate, data=payload, headers=header, cookies=cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])

response = requests.request("GET", 'https://www.kroger.com/stores?pickupStoreId=02400339', headers=header, cookies=cookie)

responsejson = response.json()
cookie['DivisionID'] = responsejson['store']['storeInformation']['divisionNumber']
cookie['StoreLocalName'] = responsejson['store']['storeInformation']['localName']
cookie['StoreCode'] = responsejson['store']['storeInformation']['storeNumber']
cookie['StoreAddress'] = urllib.parse.quote(responsejson['store']['storeInformation']['address']['addressLineOne'] + ", " + responsejson['store']['storeInformation']['address']['city'] + ", " + responsejson['store']['storeInformation']['address']['state'])
cookie['StoreZipCode'] = responsejson['store']['storeInformation']['address']['zipCode']
cookie['StoreInformation'] = urllib.parse.quote(cookie['StoreAddress'] + responsejson['store']['storeInformation']['phoneNumber'] + "," + responsejson['store']['pharmacyInformation']['phoneNumber'])
cookie['eCommPickupStore'] = responsejson['userProfile']['bannerSpecificDetails'][0]['pickupStoreNumber']
cookie['eCommPickupStoreDivision'] = responsejson['userProfile']['bannerSpecificDetails'][0]['pickupStoreDivisionNumber']

cookie = updatecookie(cookie, response.headers['set-cookie'])
response = requests.request("GET", url + storesetup, headers=header, cookies = cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])

payload = {'pickupStoreId': '02400339', 'divisionSwitch': 'true', 'catalogId': '11051', 'langId': '', 'storeId': '11151', 'URL': 'https://www.kroger.com/storecatalog/servlet/TopCategoriesDisplayView?storeId=11151&catalogId=11051&langId=-1'}
response = requests.request("GET", url + logon, params = payload, headers = header, cookies = cookie)



response = requests.request("GET", 'https://www.kroger.com/storecatalog/servlet/Logon?pickupStoreId=02400339&divisionSwitch=true&catalogId=11051&langId=&storeId=11151&URL=https://www.kroger.com/storecatalog/servlet/TopCategoriesDisplayView?storeId=11151&catalogId=11051&langId=-1', headers = header, cookies = cookie)


response = requests.request("GET",'https://www.kroger.com/storecatalog/clicklistbeta/api/items/personalized/myFavorites',headers=header)


for key, morsel in sorted(cookie.items()):
    print(key, ": ", morsel)