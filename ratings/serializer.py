from rest_framework import serializers
from .models import Profile,Project

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        
        fields = ('name', 'bio')
        


class MerchSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields=('sitename','technologies','categories','desc','link')