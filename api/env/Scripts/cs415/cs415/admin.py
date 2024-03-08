from django.contrib import admin 
from .models import AddressType, PageData, PhoneType, User, UserAddress, UserInfo, UserPhone

# Register your models here.
admin.site.register(AddressType)
admin.site.register(PageData)
admin.site.register(PhoneType)
admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(UserInfo)
admin.site.register(UserPhone)