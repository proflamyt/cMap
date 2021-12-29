from django.contrib.gis.db import models
from django.contrib.gis.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from leafapp.models import Maptype, Marker

class PointForm(ModelForm):
    class Meta:
        model = Marker
        fields = '__all__'   
    def __init__(self, *args, **kwargs):
        coordinate = kwargs['data'].pop('location', None)
        
        if coordinate:
            coordinate = coordinate.replace(',', ' ')  # remove comma, as we need single space between two numbers.
            kwargs['data']['location'] = f'SRID=4326;POINT({coordinate})'

        super(PointForm, self).__init__(*args, **kwargs)

class MapForm(ModelForm):
    class Meta:
        model = Maptype
        fields = '__all__'