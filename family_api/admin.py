from django.contrib import admin
from .models import FamilyMember

# Register your models here.
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'gender', 'is_alive', 'place_of_birth', 'date_of_death',  'occupation', 'biographical_information', 'photo']

admin.site.register(FamilyMember, FamilyMemberAdmin)