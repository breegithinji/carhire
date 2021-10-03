from django.contrib import admin
from .models import CarType, CarMake, CarModel, CarOwner, carInstance, Car, CarImage

# change admin panel information
admin.site.site_header = "Kanairo Car Hire LTD"
admin.site.site_title = "Admin | Kanairo Car Hire LTD"
admin.site.index_title = "Admin | Kanairo Car Hire LTD"

# this is to ensure that a car owner is shown with all the cars they own
class CarInline(admin.TabularInline):
  model = Car
  extra = 3

class CarOwnerAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['car_owner']}),
    (None, {'fields': ['contact_info']}),]
  inlines = [CarInline]

class ImagesInline(admin.TabularInline):
  model = CarImage
  extra = 3

class CarAdmin(admin.ModelAdmin):
  fieldsets = [('Car Details', {'fields': ['registration', 'car_type', 'car_make', 'car_model', 'car_owner', 'description']}), 
  ]
  inlines = [ImagesInline]

#Register the models here
admin.site.register(CarType)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(CarOwner, CarOwnerAdmin)
admin.site.register(carInstance)
admin.site.register(Car, CarAdmin)






