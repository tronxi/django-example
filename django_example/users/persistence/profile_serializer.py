from rest_framework import serializers

from django_example.users.persistence.custom_user import CustomUser


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
