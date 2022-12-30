from django.contrib import admin

from .models import Dania_Pizzeria
from .models import Category
from .models import Language
from .models import Configuration

# Register your models here.
admin.site.register(Configuration)
admin.site.register(Dania_Pizzeria)
admin.site.register(Category)
admin.site.register(Language)
