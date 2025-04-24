from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('book_tour/', views.book_tour, name='book_tour'),

    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('destination/', views.destination, name='destination'),
    path('package/', views.package, name='package'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),


    path('tour_list/', views.tour_list, name='tour_list'),
    path('tour_detail/<int:pk>/', views.tour_detail, name='tour_detail'),

]