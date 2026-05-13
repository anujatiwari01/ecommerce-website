from django.urls import path
from .views import homepage, aboutus,contactus,get_item,create_product,update_product,delete_product

urlpatterns = [
	path('',homepage,name='products'),
	path('aboutus/',aboutus),
	path('contact/',contactus),
	path('product/<int:id>/',get_item,name='product'),
	path('create/',create_product,name='create_product'), 
	path('update/<int:id>/',update_product,name='update_product'),
	path('delete/<int:id>/',delete_product,name='delete_product'),
	]
    
