from django.contrib import admin
from main.models import *

# Register your models here.
admin.site.register(mainx)
admin.site.register(Contact)
admin.site.register(Projects)
admin.site.register(Eduction)
admin.site.register(summery)
admin.site.register(Professional_Experience)
admin.site.register(skills)
admin.site.register(certificates)




class ContactAdmin(admin.ModelAdmin):
    # Customize the list display
    list_display = ('name', 'email', 'created_at')
    # Add a search bar
    search_fields = ('name', 'email')
    # Add filters on the sidebar
    list_filter = ('created_at',)



class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date')
