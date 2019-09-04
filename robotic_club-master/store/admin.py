from django.contrib import admin

# Register your models here.
from store.models import Item_discription,Request_item,Cart


admin.site.register(Item_discription)
admin.site.register(Request_item)
admin.site.register(Cart)