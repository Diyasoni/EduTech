from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Notes)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Todo)

