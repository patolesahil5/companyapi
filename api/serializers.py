#Creating Serializers
from api.models import Company
from rest_framework import serializers

class CompanySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"