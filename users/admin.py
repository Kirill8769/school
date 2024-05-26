from django.contrib import admin

from .models import Payment, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'city', )
    list_filter = ('city', )
    search_fields = ('email', 'city', 'phone', )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method', )
    list_filter = ('user', 'payment_date', 'payment_method', 'paid_course', 'paid_lesson', )
    search_fields = ('user', 'payment_date', )
