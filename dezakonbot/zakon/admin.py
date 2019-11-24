from django.contrib import admin
from zakon.models import AcceptedZakonModel, RegisteredZakonModel

@admin.register(AcceptedZakonModel)
class AcceptedZakonModelAdmin(admin.ModelAdmin):
    pass

@admin.register(RegisteredZakonModel)
class RegisteredZakonModelAdmin(admin.ModelAdmin):
    pass