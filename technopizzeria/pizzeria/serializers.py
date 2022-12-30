from email.policy import default
from rest_framework import serializers

from .models import Dania_Pizzeria
from .models import Category
from .models import Language
from .models import Configuration


class DaniaSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Dania_Pizzeria
        fields = '__all__'
    
class ConfigurationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Configuration
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Category
        fields = '__all__'
    
class LanguageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Language
        fields = '__all__'