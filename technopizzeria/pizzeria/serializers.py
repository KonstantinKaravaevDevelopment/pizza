from email.policy import default
from rest_framework import serializers

from .models import Dania_Pizzeria


class DaniaSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Dania_Pizzeria
        fields = '__all__'

