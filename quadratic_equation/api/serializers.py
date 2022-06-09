from rest_framework import serializers

from equation.models import Equation


class EquationSerializer(serializers.ModelSerializer):
    """ Serializer for equation. """

    class Meta:
        fields = '__all__'
        model = Equation
