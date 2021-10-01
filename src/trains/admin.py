from django.contrib import admin
from trains.models import Train


class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train

    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    list_editable = ('travel_time',)


# Зарегистриуем admin-ку
admin.site.register(Train, TrainAdmin)
