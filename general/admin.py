from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, FirstOrder, SecondOrder, ExtraServices
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('Clients', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        ('Associated Tasks', {
            'classes': ('wide',),
            'fields': ('email', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class FirstOrderDisplay(admin.ModelAdmin):
    model = FirstOrder
    list_filter = ('client', 'deadline', )
    list_display = ['client', 'complexity', 'deadline']
    fieldsets = (('Associated Tasks', {'fields': ('client',)}),)
    search_fields = ('complexity',)
    order_by = ('-deadline', )


class SecondOrderDisplay(admin.ModelAdmin):
    model = SecondOrder
    list_display = [
        'order_form',
        'subject',
        'number_of_pages',
        'reference_style',
        'reference_total',
        'pricing',
    ]


class ExtraTaskDisplay(admin.ModelAdmin):
    model = ExtraServices
    list_display = [
        'extra_task',
        'pricing'
    ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FirstOrder, FirstOrderDisplay)
admin.site.register(SecondOrder, SecondOrderDisplay)
admin.site.register(ExtraServices, ExtraTaskDisplay)
