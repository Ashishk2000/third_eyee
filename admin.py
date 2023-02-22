from django.contrib import admin
from database.models import *

# Register your models here.
admin.site.site_title = "Administration"
admin.site.site_header = "Site Administration"
admin.site.register(RemoteSite)
