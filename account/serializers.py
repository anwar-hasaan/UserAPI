from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    # Validate password
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and confirm Password mast be same!")
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 charecters")
        return data
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)