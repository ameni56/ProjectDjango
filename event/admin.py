from django.contrib import admin,messages
from .models import *




from datetime import datetime
#3)f)ii)
#  nb : Try to use StackedInline instead of TabularInline
class ParticipationInline(admin.TabularInline):
    model = participants
    readonly_fields=('date_participation',)
    extra = 1
    can_delete=False
    classes =['collapse']
# class ParticipationInline(admin.StackedInline):
#     model = participants
#     readonly_fields = ('date_participation',)
#     extra = 1
#     can_delete = False
#     classes = ['collapse']    


#3)e)
# Change state to true with actions:
def set_Accept(ModelAdmin , request , queryset):
    rows_updated =  queryset.update(state=True)
            
    if (rows_updated ==1): 
        msg = " 1 event was"

    else:
        msg = f"{rows_updated}  events were  "

    messages.success(request,f'{msg} successfully updated' )



#3)e)
# Change state to false with actions:
def set_Refuse(ModelAdmin , request , queryset):
    rows_updated =  queryset.update(state=False)
            
    if (rows_updated ==1): 
        message = " 1 event was"

    else:
        message = f"{rows_updated}  events were  "

    messages.success(request,f'{message} successfully updated' )


set_Accept.short_description = "State True"

set_Refuse.short_description = "State False"




#3)a)Inscrivez le modèle « Event » au site d’administration ;
@admin.register(Event)
#3)b)Créer la classe EventAdmin.
class EventAdmin(admin.ModelAdmin):
#3)c)ii)Définissez et personnaliser la variable list_display à fin de contrôler quels
#champs seront affichés sur la page de la liste de l’interface d’administration.
    list_display=('title', 'description' ,'image', 'evt_date','category','state', 'created_date','updated_date' ,'organisateur','event_nbr_participant')
     
#3)d)Activez les filtres dans la barre latérale droite de la page d’affichage de la liste des
#évènements avec list_filter :
    list_filter = (  
        'state','category',
        
    )


#3)e) Ajouter deux actions dans la liste des évènements qui permettent de rendre l’état
#d’un évènement « accepté » ou « refusé »  
    actions = [set_Accept , set_Refuse]

#3)f)iii)
    autocomplete_fields=['organisateur']
#3)f)ii)
    inlines =[ ParticipationInline]

    # fields =(('title','category') , 'description')
#3)c)iv)
    readonly_fields=('created_date','updated_date')
#3)f)
    fieldsets = ( 
        
        ('Event description', {
                'fields': ('title' ,'category','state','organisateur' , 'image'),
        }),
        ('Dates' , {
        'fields':('evt_date','created_date','updated_date'),
        }),
                 
                 
                 
                 )
#3)c)v)                 
    list_per_page = 2

    ordering = ['-title']

#3)c)iii)
    def event_nbr_participant(self,obj):
        count = obj.participant.count()
        return count 
    


    event_nbr_participant.short_description = 'Nombre des participants'


#3)f)ii)
admin.site.register(participants) 
