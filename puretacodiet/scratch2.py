import requests
import urllib

cookie = dict()
url = 'https://www.kroger.com'
signin = '/signin'
authenticate = '/user/authenticate'
favorites = '/storecatalog/clicklistbeta/api/items/personalized/myFavorites'
ecommercesetupurl = '/onlineshopping'
storesetup = '/storecatalog/servlet/OnlineShoppingStoreSetup'

def encode(cookie):
    encodedcookie = ''
    for key, value in cookie.items():
        encodedcookie = encodedcookie + key + '=' + value + ';'
    return encodedcookie

def printcookies(cookie):
    encodecookie = ''
    for key, value in cookie.items():
        print(key, ': ', value)


header = {
    'host': "www.kroger.com",
    'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0",
    'accept': "application/json, text/plain, */*",
    'accept-language': "en-US,en;q=0.5",
    'accept-encoding': "gzip, deflate, br",
    'referer': "https://www.kroger.com/signin?redirectUrl=/",
    'content-type': "application/json;charset=utf-8",
    'connection': "keep-alive",
    'cache-control': "no-cache"
    }

"""
response = requests.request("GET",url+signin, headers=header)
"""

payload = "{\"account\":{\"email\":\"johns10davenport@gmail.com\",\"password\":\"A7B!2#x2y\",\"rememberMe\":null},\"location\":\"\"}"

response = requests.request("POST", url + authenticate, data=payload, headers=header)

responsejson = response.json()
cookie['pid'] = response.cookies['pid']
cookie['sid'] = response.cookies['sid']
cookie['aid'] = response.cookies['aid']
cookie['aid_2'] = response.cookies['aid_2']
cookie['loggedIn'] = 'yes'
cookie['DivisionID'] = responsejson['store']['storeInformation']['divisionNumber']
cookie['StoreLocalName'] = responsejson['store']['storeInformation']['localName']
cookie['StoreCode'] = responsejson['store']['storeInformation']['storeNumber']
cookie['StoreAddress'] = urllib.parse.quote(responsejson['store']['storeInformation']['address']['addressLineOne'] + ", " + responsejson['store']['storeInformation']['address']['city'] + ", " + responsejson['store']['storeInformation']['address']['state'])
cookie['StoreZipCode'] = responsejson['store']['storeInformation']['address']['zipCode']
cookie['StoreInformation'] = urllib.parse.quote(cookie['StoreAddress'] + responsejson['store']['storeInformation']['phoneNumber'] + "," + responsejson['store']['pharmacyInformation']['phoneNumber'])
cookie['eCommPickupStore'] = responsejson['userProfile']['bannerSpecificDetails'][0]['pickupStoreNumber']
cookie['eCommPickupStoreDivision'] = responsejson['userProfile']['bannerSpecificDetails'][0]['pickupStoreDivisionNumber']
cookie['eCommPickupStoreZipCode'] = responsejson['userProfile']['bannerSpecificDetails'][0]['pickupStoreDivisionNumber']

encodedcookie = encode(cookie)
printcookies(cookie)

header['DNT'] = '1'
header['connection'] = 'keep-alive'
header['pragma'] = 'no-cache'
header['Cookie'] = encodedcookie

response = requests.request("POST", url + storesetup, headers=header)
    
    
    response = requests.request("GET", url, headers=header)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
xsrfheader = {
    'host': 'www.kroger.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.5',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.kroger.com/signin?redirectUrl=/',
    'Cookie': 'pid=c1695ea6-d4bc-44e6-8ea2-a36ab5f57fb9;'
        'sid=3fe6a36d-e668-417b-b6c6-a9e55b46c0fe;'
        'aid=84BCFE43708832BE2EE989A4CE8557020F7D10E310583C3C46D666BF8EB978875A9DB46C5B10FBD198F79D4448DAF39F4FC963FB477E54E6744040C5D60B75F6;'
        'aid_2=1504061110672|3fe6a36d-e668-417b-b6c6-a9e55b46c0fe;'
        'loggedIn=yes;'
        'DivisionID=024;'
        'StoreLocalName=Kroger;'
        'StoreCode=00224;'
        'StoreInformation=2200+Brownsboro+Rd%2C+Louisville%2C+KY%2C5028971133%2C5028948759;'
        'StoreAddress=2200+Brownsboro+Rd%2C+Louisville%2C+KY;'
        'StoreZipCode=40206;',
    'DNT' : '1',
    'connection': 'keep-alive',
    'Pragma': 'no-cache',
    'cache-control': 'no-cache'
    }

response = requests.request("GET",'https://www.kroger.com/products/api/next-basket',headers=header)

response.json()

ecommercesetuppayload = {'pickupStoreId': cookie['eCommPickupStoreDivision'] + cookie['eCommPickupStore'], 'divisionSwitch': 'true', 'divisionSwitch': 'true'}

favheaders = {
    'host': "www.kroger.com",
    'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'accept-language': "en-US,en;q=0.5",
    'accept-encoding': "gzip, deflate, br",
    'Cookie': 'WC_PERSISTENT=%2bncBuK6%2bO4JSEco9SnLOjG%2bchEA%3d%0a%3b2017%2d08%2d30+03%3a03%3a49%2e186%5f1474599693183%2d16700%5f11151;'
        'WC_SESSION_ESTABLISHED=true;'
        'WC_AUTHENTICATION_1626322=1626322%2cqes%2bzb%2fVDGFNTbnOJGtYCjTQMN0%3d;'
        'WC_ACTIVEPOINTER=%2d1%2c11151;'
        'WC_USERACTIVITY_1626322=1626322%2c11151%2cnull%2cnull%2c1504062232771%2c1504098232771%2cnull%2cnull%2cnull%2cnull%2c8mP%2bHigpuZTfHtiuXfTjOdnVyjRGCaVkvHPU8t35W9rcVgsVXDgG8fMKPjpoUGUIkZmWM1RVCyt93DDYfBH0ttLd1z4zRH2GyHyRMceaGFNI%2byrUWVbL%2fq7JV7CWYBAOmFb2e4TO8Sy9o5Ey4zrAk403dHmrbokKdf1O7CMB%2bkwOl49zEHUszVqYY%2bKaMEJMy22QlacRWhbVRWAoeksoibyd5Q8n5ia6Zohy9bS4l7I%3d;'
        'pid=c1695ea6-d4bc-44e6-8ea2-a36ab5f57fb9;'
        'sid=3051dbca-b70d-4834-9155-d20b8aa91ed0;'
        'loggedIn=yes;'
        'DivisionID=024;'
        'StoreLocalName=Kroger;'
        'StoreCode=00224;'
        'StoreInformation=2200+Brownsboro+Rd%2C+Louisville%2C+KY%2C5028971133%2C5028948759;'
        'StoreAddress=2200+Brownsboro+Rd%2C+Louisville%2C+KY;'
        'StoreZipCode=40206;'
        'XSRF-TOKEN=95292292-f5b7-4ee4-9485-9b6bc507502f;'
        'aid=84BCFE43708832BE2EE989A4CE8557020F7D10E310583C3C46D666BF8EB978879043199C25684335261B8EA2D43EE72E9EC54BC04EB5FA29EA1F49018332418A;'
        'eCommPickupStoreZipCode=40205;'
        'eCommPickupStoreDivision=024;'
        'eCommPickupStore=00339;'
        'eCommPickupStoreStreetAddress=2440 Bardstown Rd;'
        'eCommPickupStoreCity=Louisville;'
        'eCommPickupStoreState=KY;'
        'eCommPickupStoreChange=02400339;'
        'hasHomeShopOrderHistory=false;'
        'eCommPickupVanityName=Highlands%20Kroger;'
        'eCommPickupStoreTimeZone=(UTC-05%3A00)%20Eastern%20Time%20(US%20Canada)',
    'connection': "keep-alive",
    'Upgrade-Insecure-Results' : "1",
    'DNT' : '1'
    }

response = requests.request("GET",'https://www.kroger.com/storecatalog/clicklistbeta/api/items/personalized/myFavorites',headers=favheaders)
response.json()

params = {
    'divisionNumber' : '024',
    'storeNumber' : '00339'
}

response = requests.request("GET",'https://www.kroger.com/products/api/next-basket',headers=headers)

response.cookies

    // After picking store
cookie['eCommPickupStore=' + store.storeNumber, uri);
cookie['eCommPickupStoreDivision=' + store.divisionNumber, uri);
cookie['eCommPickupStoreChange=' + store.recordId, uri);
cookie['eCommPickupStoreStreetAddress=' + store.address.addressLineOne, uri);
cookie['eCommPickupStoreCity=' + store.address.city, uri);
cookie['eCommPickupStoreState=' + store.address.state, uri);
cookie['eCommPickupStoreZipCode=' + store.address.zipCode, uri);
