from pathlib import Path
from django.urls import path
from amazon.views import helloworld, mywebsite, sayhello, contactus, amazonproducts, aboutus
urlpatterns = [

    
    # path('hello',helloworld),
    # path('iti', mywebsite),
    # path('iti/<name>', sayhello),
    path('contactus', contactus),
    path('products', amazonproducts),
    path('aboutus', aboutus)
    
]
