from rest_framework import serializers

from amount.models import Amount


class AmountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Amount
        fields = '__all__'
