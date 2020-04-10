import requests
import django
import json
from io import StringIO
from puretacodiet.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from kroger import Kroger
import re
from itertools import cycle

Ingredient.objects.all().delete()
Recipe.objects.all().delete()
RecipeIngredient.objects.all().delete()
DietPlan.objects.all().delete()
Meal.objects.all().delete()
MealItem.objects.all().delete()
PlanInstance.objects.all().delete()
PlanInstanceList.objects.all().delete()
User.objects.all().delete()
Vendor.objects.all().delete()
ExternalCredential.objects.all().delete()

i1 = Ingredient(title="Sirloin Steak", calories=50, protein=10, fat=1, carbohydrates=0)
i2 = Ingredient(title="Corn Tortillia", calories=50, protein=0, fat=2, carbohydrates=10)
i3 = Ingredient(title="Onions", calories=11, protein=0, fat=2, carbohydrates=3)
r1 = Recipe(title="El Traditionale",info="later",servings=1,directions="later", calories=1, protein=1, fat=1, carbohydrates=1, weight=1)
i1.save()
i2.save()
i3.save()
r1.save()
ri1 = RecipeIngredient(ingredient=i1, uom="OZ", recipe=r1, quantity=3)
ri2 = RecipeIngredient(ingredient=i2, uom="OZ", recipe=r1, quantity=1)
ri1.save()
ri2.save()
dp1 = DietPlan(title="The Uno",description="This is only one taco a day.  Even babies eat more than that.  We don't recommend it.", quantity=1)
dp2 = DietPlan(title="The Quatro",description="Four tacos a day.  That's not a lot of tacos, but it's what I've been doing, and it's been pretty successful.", quantity=4)
dp1.save()
dp2.save()
m1 = Meal(title="John's Brunch")
m2 = Meal(title="John's Lunch")
m1.save()
m2.save()
mi1 = MealItem(meal=m1,recipe=r1, quantity=1)
mi2 = MealItem(meal=m1,recipe=r1, quantity=1)
mi3 = MealItem(meal=m2,recipe=r1, quantity=1)
mi4 = MealItem(meal=m2,recipe=r1, quantity=1)
mi1.save()
mi2.save()
mi3.save()
mi4.save()
p1 = Plan(title="John's Steak Taco Plan", description="John's basic four taco plan.", dietplan=dp2)
p1.save()
p1.meals.add(m1)
p1.meals.add(m2)
p1.save()

planinstance1 = PlanInstance(date="2018-10-16", plan=p1)
planinstance2 = PlanInstance(date="2018-10-17", plan=p1)
planinstance3 = PlanInstance(date="2018-10-18", plan=p1)
planinstance4 = PlanInstance(date="2018-10-19", plan=p1)
planinstance5 = PlanInstance(date="2018-10-20", plan=p1)
planinstance1.save()
planinstance2.save()
planinstance3.save()
planinstance4.save()
planinstance5.save()

planinstancelist = PlanInstanceList()
planinstancelist.save()
planinstancelist.planinstance.add(planinstance1)
planinstancelist.planinstance.add(planinstance2)
planinstancelist.planinstance.add(planinstance3)
planinstancelist.planinstance.add(planinstance4)
planinstancelist.planinstance.add(planinstance5)
planinstancelist.save()

kroger = Vendor(name = 'Kroger')
kroger.save()

user = User(first_name = 'John', last_name = 'Davenport', username = 'johns10')
user.set_password('A7B!2#x2y')
user.save()

userprofile = UserProfile(address1='743 E Broadway',address2='#153',city='Louisville',state='KY',zip=40202,homephone='15026016720',mobilephone='15026016720')

xc = ExternalCredential(user = user, username = 'johns10davenport@gmail.com', vendor = kroger, password = 'A7B!2#x2y')
xc.save()

krogersession = Kroger()
if krogersession.headers['X-XSRF-TOKEN'] == '':
    krogersession.getxsrftoken()

if not krogersession.getauthstate():
    krogersession.authenticate(xc.username, xc.password)

stores = krogersession.getlocalstores(userprofile.zip)
krogersession.setuponlineshopping()
response = krogersession.session.get(krogersession.urls.base + krogersession.urls.favorites)

onion = Product(vendor=kroger, sku='0000000004663')

corntortillia = Product(vendor=kroger, sku='0002733100061')
steak = Product(vendor=kroger, sku='0020235000000')
lime = Product(vendor=kroger, sku='0000000004048')
cilantro = Product(vendor=kroger, sku='0000000004889')

cilantroresponse = krogersession.session.get(krogersession.urls.base + krogersession.urls.items + '/' + cilantro.sku)
limeresponse = krogersession.session.get(krogersession.urls.base + krogersession.urls.items + '/' + lime.sku)
steakresponse = krogersession.session.get(krogersession.urls.base + krogersession.urls.items + '/' + steak.sku)
onionresponse = krogersession.session.get(krogersession.urls.base + krogersession.urls.items + '/' + onion.sku)
corntortilliaresponse = krogersession.session.get(krogersession.urls.base + krogersession.urls.items + '/' + corntortillia.sku)

cilantroquantity1 = ProductQuantity(product=cilantro, uom='Each', quantity=1)

cilantro.save()
lime.save()
steak.save()
onion.save()
corntortillia.save()

cilantroresponse.json()
limeresponse.json()
steakresponse.json()
onionresponse.json()
corntortilliaresponse.json()

cilantroresponse.json()['sizing']
limeresponse.json()['sizing']
steakresponse.json()['sizing']
onionresponse.json()['sizing']
corntortilliaresponse.json()['sizing']

cilantroresponse.json()['soldBy']
limeresponse.json()['soldBy']
steakresponse.json()['soldBy']
onionresponse.json()['soldBy']
corntortilliaresponse.json()['soldBy']
cilantroresponse.json()['orderBy']
limeresponse.json()['orderBy']
steakresponse.json()['orderBy']
onionresponse.json()['orderBy']
corntortilliaresponse.json()['orderBy']

response = krogersession.session.get(krogersession.urls.base+krogersession.urls.amprofile)
preferredstore = krogersession.session.get(krogersession.urls.base + krogersession.urls.storelocator + '/' + response.json()['bannerSpecificDetails'][0]['preferredStoreDivisionNumber'] + '/' + response.json()['bannerSpecificDetails'][0]['preferredStoreNumber'])
ecommstore = krogersession.session.get(krogersession.urls.base + krogersession.urls.storelocator + '/' + response.json()['bannerSpecificDetails'][0]['pickupStoreDivisionNumber'] + '/' + response.json()['bannerSpecificDetails'][0]['pickupStoreNumber']).json()
            
response = krogersession.session.get(krogersession.urls.base + krogersession.urls.favorites)
  
size = krogersession.buildquantityproperty(krogersession.parseqtystring(corntortilliaresponse.json()['sizing'], ' '))

cilantroquantity1 = ProductQuantity(product=cilantro, uom='Each', quantity=1)


























sizelist = []
def parseqtystring(qtystring,splitchar):
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
                    subelements = parseqtystring(element,'/')
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
                        subelements = parseqtystring(element,'/')
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

def buildquantityproperty(quantityelements):
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

for item in response.json():
    #print(item['sizing'])
    size = parseqtystring(item['sizing'], ' ')
    #print("Size", size)
    size2 = buildquantityproperty(size)
    for sizeitem in size2:
        sizeitem['name'] = item['name']
    #print("Size2", size2)
    sizelist.append(size2)


for quantityelement in sizelist:
    print("Quantity Element:")
    for item in quantityelement:
        print(item)
