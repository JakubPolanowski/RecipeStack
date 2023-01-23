from django.contrib import admin
import models
# Register your models here.


class FlavorInline(admin.StackedInline):
    model = models.Flavor


admin.site.register(models.Flavor, FlavorInline)
