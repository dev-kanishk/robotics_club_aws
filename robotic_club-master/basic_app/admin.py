from django.contrib import admin

# Register your models here.
from basic_app.models import Tokens,UserProfile,Notification


admin.site.register(Tokens)

admin.site.register(UserProfile)
admin.site.register(Notification)
