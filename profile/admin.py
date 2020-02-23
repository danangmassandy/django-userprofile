from django.contrib import admin
from django.contrib.admin import AdminSite
from django.conf.urls import url
from .models import Profile
from .views import index

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user__first_name','user__last_name','phone_number')

    def user__first_name(self, obj):
        return obj.user.first_name

    user__first_name.admin_order_field = 'user__first_name'
    user__first_name.short_description = 'First Name'

    def user__last_name(self, obj):
        return obj.user.last_name

    user__last_name.admin_order_field = 'user__last_name'
    user__last_name.short_description = 'Last Name'

    def get_queryset(self, request):
        qs = super(ProfileAdmin, self).get_queryset(request)
        return qs.exclude(user__is_superuser=True)

admin.site.register(Profile,ProfileAdmin)