from django.contrib import admin


from .models import Birthday

class BirthdayAdmin(admin.ModelAdmin):
    """Создаем модель Birthday."""
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday'
    )

    list_editable = (
        'first_name',
        'last_name',
        'birthday'
    )


admin.site.register(Birthday, BirthdayAdmin)