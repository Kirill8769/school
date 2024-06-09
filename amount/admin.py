from django.contrib import admin

from .models import Amount


@admin.register(Amount)
class AmountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'course', 'amount', )
    list_filter = ('course', )
