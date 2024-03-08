from rest_framework import serializers
from cs415.models import User, UserAddress, UserInfo, UserPhone, PhoneType, PageData, AddressType

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['user_id', 'first_name', 'last_name', 'email' , 'password', 'created_date', 'is_active']
        fields = '__all__'
class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= PageData
        fields='__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, clean_data):
        user_obj = User.objects.create(email=clean_data['email'],
                                       password=clean_data['password'])


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['user_id', 'first_name', 'last_name', 'email' , 'password', 'created_date', 'is_active']
        fields = '__all__'


class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddressType
        depth=1
        fields = '__all__'


class AddressSerializerGet(serializers.ModelSerializer):
    address_type = AddressTypeSerializer(read_only=True)
    class Meta:
        model = UserAddress
        # depth = 1
        fields = '__all__'


class AddressSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'


class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhoneType
        depth=1
        fields = '__all__'


class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddressType
        depth=1
        fields = '__all__'


class PhoneSerializerGet(serializers.ModelSerializer):
    phone_type = PhoneTypeSerializer(read_only=True)
    class Meta:
        model=UserPhone
        fields = '__all__'


class PhoneSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=UserPhone
        fields = '__all__'


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields='__all__'