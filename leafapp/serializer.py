from rest_framework_gis import serializers

from leafapp.models import Marker


class MarkerSerializer(serializers.GeoModelSerializer):
    """Marker GeoJSON serializer."""

    class Meta:
        """Marker serializer meta class."""
        model = Marker
        fields = ("id", "name", "location", "description")
        geo_field = "location"
        