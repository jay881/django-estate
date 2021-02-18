from django.db import models
from django.utils import timezone
# Create your models here.
# class login(models.model):
#
#     name = models.CharField(max_length=100)
#
# def __str__(self):
#     return self.name
class Buyer(models.Model):
    name = models.CharField(max_length=50, default='')
    gmail_id = models.EmailField(max_length=100, default='')
    password = models.CharField(max_length=50, default='')

class Seller_info(models.Model):
    name = models.CharField(max_length=50)
    gmail_id = models.EmailField(max_length=100, default='')
    password = models.CharField(max_length=50, default='')
    pan_no = models.CharField(max_length=50, default='')
    aadhar_no = models.CharField(max_length=50, default='')
    pan_card_photo = models.ImageField(upload_to='media/seller_img' , default='')
    aadhar_card_photo =  models.ImageField(upload_to='media/seller_img' , default='')
    seller_profile =  models.ImageField(upload_to='media/seller_img' , default='')

class Bungalows_info(models.Model):
    # gmail_id = models.ForeignKey(Seller_info, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=50, default='')
    longitude = models.CharField(max_length = 100, default='')
    latitude = models.CharField(max_length = 100, default='')
    ground_area = models.CharField(max_length=50, default='')
    carpet_area = models.CharField(max_length=50, default='')
    BedHK = models.CharField(max_length=50, default='')
    price = models.CharField(max_length = 100, default='')
    pic = models.ImageField(upload_to='media/bungalows_img' , default='')
    property_image_one = models.ImageField(upload_to='media/flats_img' , default='')
    property_image_tow = models.ImageField(upload_to='media/flats_img' , default='')
    property_image_three = models.ImageField(upload_to='media/flats_img' , default='')
    property_image_four = models.ImageField(upload_to='media/flats_img' , default='')


class Flats_info(models.Model):

    location = models.CharField(max_length=50, default='')
    longitude = models.CharField(max_length = 100, default='')
    latitude = models.CharField(max_length = 100, default='')
    ground_area = models.CharField(max_length=50, default='')
    carpet_area = models.CharField(max_length=50, default='')
    flate_name = models.CharField(max_length=50, default='')
    flate_no = models.CharField(max_length=50, default='')
    BedHK = models.CharField(max_length=50, default='')
    floor_no = models.CharField(max_length=50, default='')
    car_parking = models.CharField(max_length=50, default='')
    price = models.CharField(max_length = 100, default='')
    pic = models.ImageField(upload_to='media/flats_img' , default='')
    property_image_one = models.ImageField(upload_to='media/flats_img' , default='')
    property_image_tow = models.ImageField(upload_to='media/flats_img' , default='')
    property_image_three = models.ImageField(upload_to='media/flats_img' , default='')
    property_image_four = models.ImageField(upload_to='media/flats_img' , default='')
    # pic2 = models.ImageField(upload_to='media/flats_img' , default='')
    # pic3 = models.ImageField(upload_to='media/flats_img' , default='')
    # pic4 = models.ImageField(upload_to='media/flats_img' , default='')
#
class Appointment_db(models.Model):
    seller = models.ForeignKey(Seller_info, on_delete=models.CASCADE, default='')
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, default='')
    appoint_date = models.CharField(max_length = 100, default='')
    app_st = models.BooleanField(default=False)
