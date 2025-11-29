from django.urls import path
from cvapp.views import *

app_name = 'cvapp'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('portfolio', portfolio_view, name='portfolio'),
    path('portfolio/details', portfolio_d_view, name='portfolio_details'),
    path('resume', resume_view, name='resume'),
    path('service', service_view, name='service'),
    path('service/details', service_d_view, name='service_details'),
    path('starter', starter_view, name='starter'),
]
