from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer
from .models import Seller_info
from .models import Bungalows_info
from .models import Flats_info
from .models import Appointment_db
import datetime
from django.core.files.storage import FileSystemStorage

# from first_app.models import name
# Create your views here.
# def Flatsinfodb(request):
#     fladb = Flats_info.objects.all()
#     return render()

def index(request):
    return render(request,'first_app/index.html')

def home(request):
    return render(request,'first_app/home.html')


def buyer_register(request):
    name = request.POST.get('name')
    id = request.POST.get('id')
    password = request.POST.get('pass')
    b = Buyer.objects.filter(gmail_id = id)
    if b:
        return render(request, 'first_app/signup.html', {"error": "The Buyer already exists"})
    buyer = Buyer(name = name, gmail_id = id, password = password)
    buyer.save()
    return render(request, 'first_app/home.html')

def buyer_signin(request):
    id = request.POST.get('id')
    password = request.POST.get('pass')
    b = Buyer.objects.filter(gmail_id = id , password = password)
    print(b)
    if b:
        return render(request, 'first_app/home.html',{'username':b[0].name})
    return render(request, 'first_app/index.html', {"error": "id or password is incorrect"})

def buyer_signup(request):
    return render(request, 'first_app/signup.html')

def listing(request):
    bundb = Bungalows_info.objects.all()
    return render(request,'first_app/listing.html', {'bun':bundb})

def listingsflats(request):
    fladb = Flats_info.objects.all()
    return render(request,'first_app/listingsflats.html', {'fla':fladb})

def sellerlistingsflats(request):
    fladb = Flats_info.objects.all()
    return render(request,'first_app/sellerlistingsflats.html', {'fla':fladb})

def seller_register(request):
    name = request.POST.get('name')
    id = request.POST.get('id')
    password = request.POST.get('pass')
    pan_no = request.POST.get('pan_card_no')
    aadhar_no = request.POST.get('aadhar_card_no')

    pan_card_photo = request.FILES['pan_card_photo']
    fs=FileSystemStorage()
    fs.save(pan_card_photo.name,pan_card_photo)

    aadhar_card_photo = request.FILES['aadhar_card_photo']
    fs=FileSystemStorage()
    fs.save(aadhar_card_photo.name,aadhar_card_photo)

    seller_profile = request.FILES['seller_profile']
    fs=FileSystemStorage()
    fs.save(seller_profile.name,seller_profile)

    s = Seller_info.objects.filter(gmail_id = id)
    if s:
        return render(request, 'first_app/sellerregister.html', {"error": "The Seller already exists"})
    seller = Seller_info(name = name, gmail_id = id,seller_profile = seller_profile,aadhar_no =aadhar_no,pan_no = pan_no, password = password, aadhar_card_photo = aadhar_card_photo,pan_card_photo = pan_card_photo)
    seller.save()
    return render(request, 'first_app/sellerhome.html')

def seller_signin(request):
    fladb = Appointment_db.objects.all()
    id = request.POST.get('id')
    password = request.POST.get('pass')
    s = Seller_info.objects.filter(gmail_id = id , password = password)
    print(s)
    if s:
        request.session['curr_user']=s[0].gmail_id
        print(request.session['curr_user'])
        return render(request, 'first_app/sellerhome.html', {'fla':fladb})
    return render(request, 'first_app/sellersignup.html', {"error": "id or password is incorrect"})

def seller_logout(request):
    request.session['curr_user']=None
    return render(request, 'first_app/sellersignup.html')

def seller_signup(request):

    return render(request, 'first_app/sellerregister.html')

def sellersignin(request):

    return render(request,'first_app/sellersignup.html')

    # Pan_card_no = request.POST.get('pan_card_no') , Pan_card_no = Pan_card_no
    # aadhar_card_no = request.POST.get('aadhar_card_no'), aadhar_card_no= aadhar_card_no, pan_card_photo = pan_card_photo, aadhar_card_photo = aadhar_card_photo
    # pan_card_photo = request.POST.get('pan_card_photo')
    # aadhar_card_photo = request.POST.get('aadhar_card_photo')

#
# def sellersignup(request):
#     return render(request,'first_app/sellersignup.html')
#
# def sellerregister(request):
#     return render(request,'first_app/sellerregister.html')

def sellerhome(request):
    seldb = Seller_info.objects.all()
    fladb = Appointment_db.objects.all()
    return render(request,'first_app/sellerhome.html', {'fla':fladb})
    #return render(request,'first_app/sellerhome.html',{'appointdb':appo_db} ,{'sel':seldb})

def Bungalows_information(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    location = request.POST.get('location')
    longitude = request.POST.get('longitude')
    latitude = request.POST.get('latitude')
    ground_area = request.POST.get('ground_area')
    carpet_area = request.POST.get('carpet_area')
    BedHK = request.POST.get('BedHK')
    price = request.POST.get('price')
    pic = request.FILES['pic']
    fs=FileSystemStorage()
    fs.save(pic.name,pic)
    property_image_one = request.FILES['property_image_one']
    fs=FileSystemStorage()
    fs.save(property_image_one.name,property_image_one)

    property_image_tow = request.FILES['property_image_tow']
    fs=FileSystemStorage()
    fs.save(property_image_tow.name,property_image_tow)

    property_image_three = request.FILES['property_image_three']
    fs=FileSystemStorage()
    fs.save(property_image_three.name,property_image_three)

    property_image_four = request.FILES['property_image_four']
    fs=FileSystemStorage()
    fs.save(property_image_four.name,property_image_four)

    prop_bungalow = Bungalows_info(id = id,name = name, property_image_three = property_image_three, property_image_four = property_image_four ,property_image_tow = property_image_tow,property_image_one = property_image_one,location = location, longitude=longitude, latitude=latitude, ground_area= ground_area, carpet_area=carpet_area, BedHK=BedHK, price=price,pic = pic)
    prop_bungalow.save()
    return render(request, 'first_app/sellerhome.html', {"error": "Bungalows added to the database"})

def Flats_information(request):

    location = request.POST.get('location')
    longitude = request.POST.get('longitude')
    latitude = request.POST.get('latitude')
    ground_area = request.POST.get('ground_area')
    carpet_area = request.POST.get('carpet_area')
    flate_name = request.POST.get('flate_name')
    flate_no = request.POST.get('flate_no')
    BedHK = request.POST.get('BedHK')
    floor_no = request.POST.get('floor_no')
    car_parking = request.POST.get('car_parking')
    price = request.POST.get('price')

    pic = request.FILES['pic']
    fs=FileSystemStorage()
    fs.save(pic.name,pic)

    property_image_one = request.FILES['property_image_one']
    fs=FileSystemStorage()
    fs.save(property_image_one.name,property_image_one)

    property_image_tow = request.FILES['property_image_tow']
    fs=FileSystemStorage()
    fs.save(property_image_tow.name,property_image_tow)

    property_image_three = request.FILES['property_image_three']
    fs=FileSystemStorage()
    fs.save(property_image_three.name,property_image_three)

    property_image_four = request.FILES['property_image_four']
    fs=FileSystemStorage()
    fs.save(property_image_four.name,property_image_four)

    prop_flats = Flats_info(location = location , property_image_three = property_image_three, property_image_four = property_image_four ,property_image_tow = property_image_tow, longitude=longitude, latitude=latitude, ground_area= ground_area, carpet_area=carpet_area, flate_name=flate_name, flate_no = flate_no , BedHK=BedHK, floor_no=floor_no, car_parking = car_parking, price = price,pic = pic , property_image_one = property_image_one,)
    prop_flats.save()
    return render(request, 'first_app/sellerhome.html', {"error": "Flats added to the database"})

def add_appoint(request):
    fladb = Appointment_db.objects.all()
    seller_id = request.POST.get('seller')
    seller= Seller_info.objects.filter(gmail_id = seller_id)
    buyer_id = request.POST.get('buyer')
    buyer = Buyer.objects.filter(gmail_id = buyer_id)
    appoint_date = request.POST.get('appoint_date')
    # date_time_obj = datetime.datetime.strptime(appoint_date, '%y/%m/%d %H:%M:%S')
    if len(seller)<=0 or len(buyer)<=0:
        return render(request, 'first_app/sellerhome.html', {"error": "Appointment error"})
    appoint_db = Appointment_db(seller = seller[0] , buyer = buyer[0],appoint_date=appoint_date)
    appoint_db.save()
    return render(request, 'first_app/home.html', {"error": "Appointment set"})


# def images(request):
#     return render(request, 'first_app/images.html')
#
# def images_add(request):
#     image = request.POST.get('image')
#     img_db = images(image = image)
#     img_db.save()
#     return render(request, 'first_app/images.html', {"error": "Flats added to the database"})
