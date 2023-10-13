from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_date):
        password = validated_date.pop('password', None)
        instance = self.Meta.model(**validated_date)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        
        return instance