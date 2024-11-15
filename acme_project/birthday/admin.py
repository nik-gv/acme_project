from django.contrib import admin


from .models import Birthday, Tag


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


class TagAdmin(admin.ModelAdmin):
    """Создаем модель Tag."""
    list_display = (
        'id',
        'tag',
    )

    list_editable = (
        'tag',
    )


admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag, TagAdmin)
