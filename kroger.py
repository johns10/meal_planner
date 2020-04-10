import requests
from collections import namedtuple
from io import StringIO
from http.cookiejar import Cookie, CookieJar 
import json
import datetime

class Kroger(object):
    def __init__(self):
        self.urls = namedtuple
        self.urls.base = 'https://www.kroger.com'
        self.urls.signin = '/signin'
        self.urls.authenticate = '/user/authenticate'
        self.urls.getauthstate = '/user/getAuthenticationState'
        self.urls.favorites = '/storecatalog/clicklistbeta/api/items/personalized/myFavorites'
        self.urls.ecommercesetupurl = '/onlineshopping'
        self.urls.storesetup = '/storecatalog/servlet/OnlineShoppingStoreSetup'
        self.urls.nextbasket = '/products/api/next-basket'
        self.urls.toggles = '/basket/api/toggles'
        self.urls.logon = '/storecatalog/servlet/Logon'
        self.urls.firstname = '/profile/getFirstNameFromSession'
        self.urls.getauthstate = '/user/getAuthenticationState'
        self.urls.pickstore = '/account/pickStore'
        self.urls.amprofile = '/accountmanagement/api/profile'
        self.urls.clbprofile = '/storecatalog/clicklistbeta/api/profile'
        self.urls.stores = '/stores'
        self.urls.storelocator = '/accountmanagement/api/store-locator'
        self.urls.addToCart = '/storecatalog/clicklistbeta/api/cart/item'
        self.urls.cart = '/storecatalog/clicklistbeta/api/cart'
        self.urls.items = '/storecatalog/clicklistbeta/api/items/upc'
        self.headers = {
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
        self.session = requests.Session()
        self.session.headers.update(self.headers)        
    def getauthstate(self):
        return self.session.get(self.urls.base + self.urls.getauthstate).json()['authenticated']
    def getxsrftoken(self):
        self.session.get(self.urls.base + self.urls.nextbasket)
        self.session.headers.update({'X-XSRF-TOKEN':self.session.cookies['XSRF-TOKEN']})
    def authenticate(self, username, password):
        auth = {}
        auth['account'] = {}
        auth['account']['email'] = username
        auth['account']['password'] = password
        auth['account']['rememberMe'] = True
        auth['location'] = ''
        authio = StringIO()
        json.dump(auth, authio)
        payload = authio.getvalue()
        response = self.session.post(self.urls.base + self.urls.authenticate, data=payload)
        self.session.cookies.set_cookie(Cookie(version=0, name='StoreLocalName', value=response.json()['store']['storeInformation']['localName'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
        self.session.cookies.set_cookie(Cookie(version=0, name='StoreCode', value=response.json()['store']['storeInformation']['localName'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
        self.session.cookies.set_cookie(Cookie(version=0, name='StoreAddress', value=(response.json()['store']['storeInformation']['address']['addressLineOne'].replace(' ', '+') + ",+" + response.json()['store']['storeInformation']['address']['city'].replace(' ', '+') + ",+" + response.json()['store']['storeInformation']['address']['state'].replace(' ', '+')), port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
        self.session.cookies.set_cookie(Cookie(version=0, name='StoreInformation', value=(response.json()['store']['storeInformation']['address']['addressLineOne'].replace(' ', '+') + ",+" + response.json()['store']['storeInformation']['address']['city'].replace(' ', '+') + ",+" + response.json()['store']['storeInformation']['address']['state'].replace(' ', '+')+response.json()['store']['storeInformation']['phoneNumber'] + "," + response.json()['store']['pharmacyInformation']['phoneNumber']), port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
        self.session.cookies.set_cookie(Cookie(version=0, name='StoreZipCode', value=response.json()['store']['storeInformation']['address']['zipCode'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
    def getlocalstores(self, zip):
        payload = {'address': str(zip),'maxResults':'5','radius':'300','storeFilters':'94'}
        stores = self.session.get(self.urls.base + self.urls.stores, params=payload)
        return(stores.json())
    def setuponlineshopping(self):
        pickstore = {}
        logon = {}
        profile = self.session.get(self.urls.base + self.urls.amprofile)        
        ecommstore = self.session.get(self.urls.base + self.urls.storelocator + '/' + profile.json()['bannerSpecificDetails'][0]['pickupStoreDivisionNumber'] + '/' + profile.json()['bannerSpecificDetails'][0]['pickupStoreNumber']).json()
        self.session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStoreDivision', value=ecommstore['managementDivisionNumber'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
        self.session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStore', value=ecommstore['storeNumber'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
        self.session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStoreStreetAddress', value=ecommstore['addressLineOne'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
        self.session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStoreCity', value=ecommstore['city'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
        self.session.cookies.set_cookie(Cookie(version=0, name='eCommPickupStoreZipCode', value=ecommstore['zipCode'], port=None, port_specified=False, domain='.kroger.com', domain_specified=False, domain_initial_dot=True, secure=False, expires = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp()), discard = False, path = '/', path_specified = True, comment = None, comment_url = None, rest = False))
        self.session.get(self.urls.base + self.urls.storesetup)
        pickstore['divisionNumber'] = ecommstore['managementDivisionNumber']
        pickstore['storeNumber'] = ecommstore['storeNumber']
        pickstore['storeType'] = 'pick'
        psio = StringIO()
        json.dump(pickstore, psio)
        payload = psio.getvalue()
        self.session.post(self.urls.base + self.urls.pickstore, data=payload)
        logon['pickupStoreId'] = ecommstore['managementDivisionNumber'] + ecommstore['storeNumber']
        logon['divisionSwitch'] = True
        logon['catalogId'] = '11051'
        logon['langId'] = ''
        logon['storeId'] = '11151'
        lio = StringIO()
        json.dump(logon, lio)
        payload = lio.getvalue()
        self.session.get(self.urls.base + self.urls.logon, params=payload)
    def getproductinfo(self, sku):
        response = self.session.get(self.urls.base + self.urls.items + '/' + sku).json()
    def parseqtystring(self, qtystring,splitchar):
        quantityelement = {}
        qtydictlist = []
        quantityelements = []
        elements = qtystring.split(splitchar)
        lastquantityelement = {'value':'','type':''}
        #print("Elements:", elements)
        for element in elements:
            #print("Element:", element)
            #This case is for integer quantity
            try:
                int(element)
                #print("Integer")
                quantityelement = {}
                quantityelement['value'] = int(element)
                quantityelement['type'] = 'quantity'
                lastquantityelement = quantityelement
                quantityelements.append(quantityelement)
            except:
                #This case is for float quantity
                try:
                    float(element)
                    #print("Float")
                    quantityelement = {}
                    quantityelement['value'] = float(element)
                    quantityelement['type'] = 'quantity'
                    lastquantityelement = quantityelement
                    quantityelements.append(quantityelement)
                except:
                    #This case is for strings
                    #print("String")
                    if len(element.split('/')) == 2:
                        #This case detects strings where it splits two different quantity indicators
                        subelements = self.parseqtystring(element,'/')
                        #print("Subelements", subelements)
                        #This case detects where it detects two quantity values (typically a fraction)
                        if ((subelements[0]['type'] == 'quantity') and (subelements[1]['type'] == 'quantity')):
                            quantity = subelements[0]['value'] / subelements[1]['value']
                            quantityelement = {}
                            quantityelement['value'] = quantity
                            quantityelement['type'] = 'quantity'
                            quantityelements.append(quantityelement)
                        #This case detects where it's a quantity, unit, quantity, unit pair.  Typical split.
                        elif ((subelements[0]['type'] == 'unit') and (subelements[1]['type'] == 'quantity')):
                            #print("here", subelements[0], subelements[1])
                            quantityelements.append(subelements[0])                            
                            quantityelements.append(subelements[1])
                        elif ((subelements[0]['type'] == 'quantity') and (subelements[1]['type'] == 'unit')):
                            pass
                    elif len(element.split('/')) == 1:
                        #print("Single")
                        #This is where there is no slash in the string
                        if any(char.isdigit() for char in element):
                            #print("Mixed")
                            #This one finds a mixed character string with numbers and letters.  Represents a concatenated quantity unit pair.  It splits them up
                            mo = re.search(r'\d(?!.*\d)',element)
                            element = element[:mo.start(0)+1] + '/' + element[mo.start(0)+1:]
                            subelements = self.parseqtystring(element,'/')
                            if ((subelements[0]['type'] == 'quantity') and (subelements[1]['type'] == 'quantity')):
                                #print("Here", subelements[0], subelements[1])
                                quantity = subelements[0]['value'] / subelements[1]['value']
                                quantityelement = {}
                                quantityelement['value'] = quantity
                                quantityelement['type'] = 'quantity'
                                quantityelements.append(quantityelement)
                            elif ((subelements[0]['type'] == 'quantity') and (subelements[1]['type'] == 'unit')):
                                #print("Mixed qty/unit pair", subelements[0], subelements[1])
                                quantityelements.append(subelements[0])                            
                                quantityelements.append(subelements[1])
                                lastquantityelement = subelements[1]
                                #print(lastquantityelement)
                        else:
                            #print("Homogeneous")
                            #print("Last", lastquantityelement)
                            #print("current", element)
                            if lastquantityelement['type'] == 'unit':
                                #print("Got Duplicate Unit", element)
                                #print(lastquantityelement['value'] + ' ' + element)
                                lastquantityelement['value'] = lastquantityelement['value'] + ' ' + element
                            else:
                                #print("Base Case")
                                #print("Base Case Element", element)
                                quantityelement = {}
                                quantityelement['value'] = element
                                quantityelement['type'] = 'unit'
                                lastquantityelement = quantityelement
                                quantityelements.append(quantityelement)
                    #print("Last", lastquantityelement, "Current", quantityelement)
                    """elif ((lastquantityelement['type'] == 'quantity') and (quantityelement['type'] == 'unit')):
                        print("Got a legit case")
                        qtydict = {}
                        qtydict['quantity'] = lastquantityelement['value']
                        qtydict['unit'] = element['value']
                        quantityelements.append(qtydict)"""
            #print("Quantity Elements", quantityelements)
        if((len(quantityelements) == 1) and (quantityelements[0]['type'] == 'unit')):
            quantityelement = {}
            quantityelement['value'] = 1
            quantityelement['type'] = 'quantity'
            quantityelements = [quantityelement] + quantityelements
        return quantityelements
    def buildquantityproperty(self, quantityelements):
        lastquantityelement = {'value':'','type':''}
        qtydictlist = []
        for quantityelement in quantityelements:
            #print("Last:", lastquantityelement, "Current:", quantityelement)
            if ((lastquantityelement['type'] == 'quantity') and (quantityelement['type'] == 'unit')):
                #print("Got a legit case")
                qtydict = {}
                qtydict['quantity'] = lastquantityelement['value']
                qtydict['unit'] = quantityelement['value']
                #print(qtydict)
                qtydictlist.append(qtydict)
            lastquantityelement = quantityelement 
        return(qtydictlist)