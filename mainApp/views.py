from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import *

def homePage(Request):
    return render(Request,"index.html")

def aboutPage(Request):
    return render(Request,"about.html")

def blogPage(Request):
    blsdata = BlogPost.objects.all().order_by("id").reverse()[:10]
    bldata = BlogPost.objects.all().order_by("id").reverse()
    paginator = Paginator(bldata,2)
    
    page_number = Request.GET.get("page")
    bldatafinal = paginator.get_page(page_number)
    total_pages = bldatafinal.paginator.num_pages
    totalPagelist = [n+1 for n in range(total_pages)]
    current_page = bldatafinal.number
    page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"blog.html",{"bldatafinal":bldatafinal,"totalPagelist":totalPagelist,"page_range":page_range,"blsdata":blsdata})

def blogDetailPage(Request,id):
    blddata = BlogPost.objects.get(id=id)
    blsdata = BlogPost.objects.all().order_by("id").reverse()[:10]
    return render(Request,"blog-detail.html",{"blddata":blddata,"blsdata":blsdata})

def eventPage(Request):
    evdata = EventPost.objects.all().order_by("id").reverse()
    evsdata = EventPost.objects.all().order_by("id").reverse()[:10]
    paginator = Paginator(evdata,2)
    
    page_number = Request.GET.get("page")
    evdatafinal = paginator.get_page(page_number)
    total_pages = evdatafinal.paginator.num_pages
    totalPagelist = [n+1 for n in range(total_pages)]
    current_page = evdatafinal.number
    page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"event.html",{"evdatafinal":evdatafinal,"totalPagelist":totalPagelist,"page_range":page_range,"evsdata":evsdata})

def eventDetailPage(Request,id):
    evddata = EventPost.objects.get(id=id)
    evsdata = EventPost.objects.all().order_by("id").reverse()[:10]
    return render(Request,"event-detail.html",{"evddata":evddata,"evsdata":evsdata})

def galleryPage(Request):
    gldata = Gallery.objects.all().order_by("id").reverse()
    paginator = Paginator(gldata,2)
    
    page_number = Request.GET.get("page")
    gldatafinal = paginator.get_page(page_number)
    total_pages = gldatafinal.paginator.num_pages
    totalPagelist = [n+1 for n in range(total_pages)]
    current_page = gldatafinal.number
    page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"gallery.html",{"gldatafinal":gldatafinal,"totalPagelist":totalPagelist,"page_range":page_range})

def contactPage(Request):
    if(Request.method=="POST"):
        cd = ContactDetail()
        cd.name = Request.POST.get("name")
        cd.phone = Request.POST.get("phone")
        cd.email = Request.POST.get("email")
        cd.company = Request.POST.get("company")
        cd.message = Request.POST.get("message")
        cd.save()
        messages.success(Request,"Form Submitted Successfully !!!")
    return render(Request,"contact.html")

def newsletterSubscription(Request):
    if(Request.method=="POST"):
        ns = NewsletterSubscription()
        ns.email = Request.POST.get("email")
        if(NewsletterSubscription.objects.filter(email=ns.email)):
            messages.success(Request,"Already Subscribed !!!")
        else:
            ns.save()
            messages.success(Request,"Thankyou For Your Subscription !!!")
    return redirect("/")
