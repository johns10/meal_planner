import requests
import urllib
from http.cookies import SimpleCookie
from http.cookiejar import Cookie, CookieJar 

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

def sacv(cookie):
    cookie['DivisionID'] = responsejson['store']['storeInformation']['divisionNumber']
    cookie['StoreLocalName'] = responsejson['store']['storeInformation']['localName']
    cookie['StoreCode'] = responsejson['store']['storeInformation']['storeNumber']
    cookie['StoreAddress'] = urllib.parse.quote(responsejson['store']['storeInformation']['address']['addressLineOne'] + ", " + responsejson['store']['storeInformation']['address']['city'] + ", " + responsejson['store']['storeInformation']['address']['state'])
    cookie['StoreZipCode'] = responsejson['store']['storeInformation']['address']['zipCode']
    cookie['StoreInformation'] = urllib.parse.quote(cookie['StoreAddress'] + responsejson['store']['storeInformation']['phoneNumber'] + "," + responsejson['store']['pharmacyInformation']['phoneNumber'])
    cookie['eCommPickupStore'] = '00339'
    cookie['eCommPickupStoreDivision'] = '024'
    cookie['eCommPickupStoreZipCode'] = '40205'
    cookie['eCommPickupStoreStreetAddress'] = '2440+Bardstown+Rd'
    cookie['eCommPickupStoreCity'] = 'Louisville'
    cookie['eCommPickupStoreState'] = 'KY'
    cookie['eCommPickupStoreChange'] = '02400339'
    cookie['dtPC'] = '401091019_662h19'
    cookie['dtSa'] = ''
    cookie['dtLatC'] = '1'
    cookie['s_invisit'] = 'true'
    cookie['s_nr'] = '1507595621122-New'
    cookie['undefined_s'] = 'First%20Visit'
    cookie['s_vnum'] = '1510187477091%26vn%3D1'
    cookie['s_invisit'] = 'true'
    cookie['s_ppvl'] = 'Kroger%2C23%2C23%2C480%2C1680%2C268%2C1680%2C1050%2C1%2CP'
    cookie['s_ppv'] = 'Kroger%2C41%2C24%2C838%2C1680%2C268%2C1680%2C1050%2C1%2CP'
    cookie['s_vi'] = '[CS]v1|2CEE0A6905078D42-4000011540000967[CE]'
    cookie['s_cc'] = 'true'
    cookie['s_fid'] = '2E9ABC94791F739E-0E0B1152053D1798'
    cookie['contextualized'] = 'ttffff'
    cookie['DSLV'] = 'Mon%20Oct%2009%202017%2020%3A31%3A20%20GMT-0400%20(Eastern%20Standard%20Time)'
    cookie['UMID'] = '3db7efd3-a8c0-418f-8150-68259dbbbfaa'
    cookie['s_sq'] = '%5B%5BB%5D%5D'
    #cookie['ak_bmsc'] = 'AD10429C78825DC677B20188C4B7439C173FE3E1222D0000CD14DC59605F1532~plRBDhh7fPBlzNoVoR5hU/TiB5zeZUPAZVrUimLeWCQThatqzjEYxO9OUInLEqMB8totNK8Nu4uF4PO1OIRWu9+436rvx85evjIUDnom5ZD+BNFucAuXcycihdn1rULKKM1WmQtEivjgvazqWT5mPFZ3BtXVyy0ceroeLJ2UVFIB7aCaQCOMJBY3RYWMeTmLT6vtQsEb8cGqom6E8YjB2WklW1ookkTnkQjQUdF95ZgZYD0MjMTOfAnrGAhMmXvrpN'
    #cookie['AMCVS_371C27E253DB0F910A490D4E%40AdobeOrg'] = '2096510701%7CMCIDTS%7C17450%7CMCMID%7C57585543606318407516187465421381115766%7CMCAID%7C2CEE15568507C97E-40000104E00019FA%7CMCOPTOUT-1507608272s%7CNONE%7CvVersion%7C2.0.0'
    #cookie['bm_sv'] = 'CF7F93FD56785BD7D4669B15197BAE4C~2+thJfULoRWvQLXRThxcO0zd3mX9sC17GSanHKYqv38PLRP8zSKGU3UHUUT6tUNZ2vq7MJhZJt0L0NqEhFAVxE6Ey2BoyGxjYqCWwz2DvA48ufJp1bLpkSajccZsXV9/DVAdMYXtkjp6+kq//8sZSTNemyYS/IPqXTBv+GQkCXY='
    #cookie['AMCV_371C27E253DB0F910A490D4E%40AdobeOrg'] = '2096510701%7CMCIDTS%7C17450%7CMCMID%7C64644216016870802534087881601702139046%7CMCAID%7C2CEE0A6905078D42-4000011540000967%7CMCOPTOUT-1507602677s%7CNONE%7CvVersion%7C2.0.0'

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

#Get XSRF Token
response = requests.request("GET", url + nextbasket, headers=header, cookies = cookie)
cookie = updatecookie(cookie, response.headers['set-cookie'])
#encodedcookie = encode(cookie)
#header['cookie'] = encodedcookie
header['X-XSRF-TOKEN'] = cookie['XSRF-TOKEN']
#printcookie(cookie)
print(response)
#Authenticate
payload = "{\"account\":{\"email\":\"johns10davenport@gmail.com\",\"password\":\"A7B!2#x2y\",\"rememberMe\":null},\"location\":\"\"}"
response = requests.request("POST", url + authenticate, data=payload, headers=header, cookies = cookie)
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

for item in response.cookies:
    print(item)