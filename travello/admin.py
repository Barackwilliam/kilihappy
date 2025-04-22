from django.contrib import admin
from .models import Destination,Service,Team,User_Testimonial,Package,Step_for_booking,Gallery,About_This_Organization,Booking_Report,Contact_Message

# Register your models here.

#admin.site.register(Destination)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('Offer_in_percent', 'image', 'location')
    search_fields = ('location',)

@admin.register(Service)
class ServerceAdmin(admin.ModelAdmin):
    list_display = ('Title', 'description', 'image')
    search_fields = ('Title','description')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('Full_name', 'image', 'designation','facebook_link','twitter_link','instagram_link')
    search_fields = ('Full_name','designation')


@admin.register(User_Testimonial)
class User_TestimonialAdmin(admin.ModelAdmin):
    list_display = ('Full_name', 'image', 'description','country')
    search_fields = ('Full_name','country')
    

@admin.register(Step_for_booking)
class Step_for_bookingAdmin(admin.ModelAdmin):
    list_display = ('Title', 'image', 'description')
    search_fields = ('location','designation')
    

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('number_of_people', 'image', 'location','number_of_day','description','price')
    search_fields = ('location','description')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('Title', 'image')
    search_fields =  ('Title', 'image')


@admin.register(About_This_Organization)
class About_This_OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title','content','mission','vision', 'image')
    search_fields =  ('title','content', 'image')


@admin.register(Booking_Report)
class Booking_ReportAdmin(admin.ModelAdmin):
    list_display = ('name','email','datetime','destination', 'message','created_at')
    search_fields =  ('name','email', 'message','destination')



@admin.register(Contact_Message)
class Contact_MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message','created_at')
    search_fields =  ('name','email', 'subject')

