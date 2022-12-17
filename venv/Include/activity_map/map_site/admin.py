from django.contrib import admin
from .models import Event, EventImg
# Register your models here.

class ImgInLine(admin.StackedInline):
    model = EventImg
    extra = 3


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "dt_of_start")
    list_display_links = ("name",)
    list_filter = ('name', 'dt_of_start', 'dt_of_end')
    inlines = [ImgInLine]


