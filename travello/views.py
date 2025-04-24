from django.shortcuts import render
from .models import Service,Destination,Package,Step_for_booking,Team,User_Testimonial,Gallery,About_This_Organization
#from .models import Destination

# Create your views here.

def index(request):
    services = Service.objects.all()[:3]
    destination = Destination.objects.all()[:3]
    package = Package.objects.all()[:3]
    abouts = About_This_Organization.objects.all()[:1]
    step =  Step_for_booking.objects.all()[:3]
    teams = Team.objects.all()[:3]
    testimonial = User_Testimonial.objects.all()[:3]
    gallery = Gallery.objects.all()

    context = {
        'services':services,
        'destination':destination,
        'package':package,
        'step':step,
        'teams':teams,
        'testimonial':testimonial,
        'gallery':gallery,
        'abouts':abouts
    }

    return render(request, 'index.html',context)


def booking(request):
    destination = Destination.objects.all()[:3]
    step =  Step_for_booking.objects.all()
    gallery = Gallery.objects.all()


    context = { 
    'step':step,
    'gallery':gallery,
    'destination':destination


    }

    return render(request, 'booking.html',context)

def destination(request):
    destination = Destination.objects.all()
    gallery = Gallery.objects.all()

    context = { 
    'destination':destination,
    'gallery':gallery


    }

    return render(request, 'destination.html',context)

def service(request):
    services = Service.objects.all()
    gallery = Gallery.objects.all()

    testimonial = User_Testimonial.objects.all()

    context = { 
   'services':services,
    'testimonial':testimonial,
    'gallery':gallery

  
    }
    return render(request, 'service.html',context)

def team(request):
    teams = Team.objects.all()
    gallery = Gallery.objects.all()

    context = { 
      'teams':teams,
        'gallery':gallery

    }

    return render(request, 'team.html',context)

def package(request):
    destination = Destination.objects.all()[:3]
    package = Package.objects.all()
    gallery = Gallery.objects.all()

    step =  Step_for_booking.objects.all()[:3]

    context = { 
    'package':package,
    'step':step,
    'gallery':gallery,
    'destination':destination




    }

    return render(request, 'package.html',context)

def testimonial(request):
    testimonial = User_Testimonial.objects.all()
    gallery = Gallery.objects.all()

    context = { 
    'testimonial':testimonial,
    'gallery':gallery


    }

    return render(request, 'testimonial.html',context)


from django.contrib import messages
from .models import Contact_Message

def contact(request):
    gallery = Gallery.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            Contact_Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all the fields.")

    context = {
        'gallery': gallery,
    }
    return render(request, 'contact.html', context)

def about(request):
    abouts = About_This_Organization.objects.all()[:1]


    context = { 
    'abouts':abouts
    }
    return render(request, 'about.html',context)


# def about_us(request):
#     abouts = About_This_Organization.objects.all()
#     return render(request, 'test.html',{'abouts':abouts})


from datetime import datetime
from .models import Booking_Report
from django.contrib import messages

def book_tour(request):
    destination = Destination.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        datetime_str = request.POST.get('datetime')  # "2025-04-22T14:30"
        destination = request.POST.get('destination')
        message = request.POST.get('message')

        try:
            datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')  # fix hapa
            Booking_Report.objects.create(
                name=name,
                email=email,
                datetime=datetime_obj,
                destination=destination,
                message=message
            )
            messages.success(request, 'Your booking has been submitted successfully!')
        except ValueError:
            messages.error(request, 'Invalid date and time format.')

    return render(request, 'booking_form.html',{'destination': destination})


from django.shortcuts import render, get_object_or_404
from .models import Tour


def tour_list(request):
    tours = Tour.objects.all()

    location = request.GET.get('location')
    tour_type = request.GET.get('type')

    if location:
        tours = tours.filter(location__icontains=location)
    if tour_type:
        tours = tours.filter(tour_type__iexact=tour_type)

    # Collect unique tour types for dropdown
    tour_types = Tour.objects.order_by('tour_type').values_list('tour_type', flat=True).distinct()

    return render(request, 'tour_list.html', {'tours': tours, 'tour_types': tour_types})

def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, 'tour_detail.html', {'tour': tour})
