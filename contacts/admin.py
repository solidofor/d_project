from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name','listing', 'email', 'phone', 'contact_date')
    list_display_links = ('id','name')
    # list_filter = ('realtor',)
    search_fields = ('name','message')
    list_per_page = 25
    # sortable_by = 
admin.site.register(Contact,ContactAdmin)
