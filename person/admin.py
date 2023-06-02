from django.contrib import admin
from .models import Person
# Register your models here.

#2)a)Inscrivez le modèle « Person » au site d’administration comme suit :admin.site.register(Person).
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
#2)b)Définissez la classe ResearchPerson qui permet de faire la recherche d’une
#personne selon son username : search_fields=[&#39;username&#39;].   
    search_fields = ['username']
   