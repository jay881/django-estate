from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('home',views.home, name= 'home'),

    path('signup', views.buyer_signup,name= 'signup'),

    path('register_buyer', views.buyer_register,name='register_buyer'),

    path('signin_buyer', views.buyer_signin,name='signin_buyer'),

    path('listing', views.listing,name='listing'),

    path('listingsflats', views.listingsflats,name='listingsflats'),

    path('sellerlistingsflats', views.sellerlistingsflats,name='sellerlistingsflats'),

    path('register_seller', views.seller_register,name='register_seller'),

    path('signin_seller', views.seller_signin,name='signin_seller'),

    path('sellersignin', views.sellersignin,name='sellersignin'),

    path('sellersignup', views.seller_signup,name='sellersignup'),
    #
    # path('sellerregister', views.sellerregister,name='sellerregister'),
    path('seller_logout',views.seller_logout,name='seller_logout'),

    path('sellerhome', views.sellerhome,name='sellerhome'),

    path('addbungalows', views.Bungalows_information,name='addbungalows'),

    path('addflats',views.Flats_information,name='addflats'),

    path('Appointments',views.add_appoint,name='Appointments'),
    # path('images',views.images,name='images'),
    #
    # path('saveimages',views.images_add,name='saveimages'),
    ]   +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
