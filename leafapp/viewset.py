from rest_framework import viewsets
from rest_framework_gis import filters

from leafapp.models import Marker
from leafapp.serializer import MarkerSerializer


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer


# calculate kingdom size
# count numbers of castle in kingdom
# 