from django.shortcuts import render

def index_view(request):
    return render(request,'cvapp/index.html')

def about_view(request):
    return render(request,'cvapp/about.html')

def contact_view(request):
    context = {'country':'Iran','city':'Tehran','phonenum1':'+989123456789','phonenum2':'+9891023456789','gmil1':'otadiparsa2@gmail.com','gmial2':'otparsa@gmial.com'}
    return render(request,'cvapp/contact.html',context)

def portfolio_view(request):
    return render(request,'cvapp/portfolio.html')

def portfolio_d_view(request):
    return render(request,'cvapp/portfolio-details.html')

def resume_view(request):
    return render(request,'cvapp/resume.html')

def service_view(request):
    return render(request,'cvapp/services.html')

def service_d_view(request):
    return render(request,'cvapp/service-details.html')

def starter_view(request):
    return render(request,'cvapp/starter-page.html')

