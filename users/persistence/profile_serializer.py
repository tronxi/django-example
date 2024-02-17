from rest_framework import serializers

from users.persistence.custom_user import CustomUser


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
