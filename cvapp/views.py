from django.shortcuts import render

def index_view(request):
    return render(request,'cvapp/index.html')

def about_view(request):
    return render(request,'cvapp/about.html')

def contact_view(request):
    return render(request,'cvapp/contact.html')

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

