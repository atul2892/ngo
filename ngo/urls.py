from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homePage),
    path("about/", views.aboutPage),
    path("blog/", views.blogPage),
    path("blog-detail/<int:id>/", views.blogDetailPage),
    path("event/", views.eventPage),
    path("event-detail/<int:id>/", views.eventDetailPage),
    path("gallery/", views.galleryPage),
    path("contact/", views.contactPage),
    path("newsletter/", views.newsletterSubscription),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
