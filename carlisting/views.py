from django.shortcuts import render
from .models import CarMake, carInstance, CarModel, CarType, Car, CarImage
# Create your views here.

# app_name = carlisting
def index(request):
    """View function to specify the site hompage"""

    #generate a count of all the cars in the system'
    cars_count = Car.objects.all().count()
    car_instance_count = carInstance.objects.all().count()

    #count the number of available cars
    num_cars_available = carInstance.objects.filter(status__exact = 'a').count()

    number_of_visits = request.session.get('number_of_visits', 0)
    request.session['number_of_visits'] = number_of_visits + 1


    # cars details
    cars = Car.objects.all()
    images = CarImage.objects.all()

    #Context Specifies how the data will be presented in the rendered view
    context = {
        'cars_count': cars_count,
        'num_cars_available': num_cars_available,
        'car_instance_count': car_instance_count,
        'number_of_visits': number_of_visits,
        'cars': cars,
        'images': images
        # 'num_toyota': num_toyota,
    }

    #Render a HTML file, index.html containing the data in the context
    return render(request, 'index.html', context=context)

def all_cars(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    
    return render(request, 'allcars.html', context=context)

def toyota_cars(request):
    toyotas = Car.objects.filter(car_make='Toyota')
    context = {
        'toyotas': toyotas
    }

    return render(request, 'toyotas.html', context=context)

def car_details(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        images = CarImage.objects.filter(car=car_id)
        # url1 = CarImage.objects.filter(car=car_id)[0].car_img.url
    except Car.DoesNotExist:
        raise Http404("Car does not exist")
    
    return render(request, 'cardetails.html', { 'car': car, 'images': images })

def cars_make_sb(request):
    makes = CarMake.objects.all()
    context = {
        'makes': makes
    }

    return render(request, 'partials/_sidebar.html', context)