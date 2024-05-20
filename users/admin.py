from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'city', )
    list_filter = ('city', )
    search_fields = ('email', 'city', 'phone', )
