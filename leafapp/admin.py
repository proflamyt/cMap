from django.contrib.gis import admin

from leafapp.models import Author, Maptype, Marker, Novel

admin.site.register(Maptype)
admin.site.register(Novel)
admin.site.register(Author)
@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location")