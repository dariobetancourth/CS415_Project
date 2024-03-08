from django.db import models


class AddressType(models.Model):
    address_type_id = models.AutoField(primary_key=True)
    address_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'AddressType'

    def __str__(self):
        return self.address_type

class PageData(models.Model):
    page_data_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=25)
    page_title = models.CharField(max_length=25)
    page_description = models.CharField(max_length=150)
    page_picture = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PageData'

    def __str__(self):
        return self.page_name

class PhoneType(models.Model):
    phone_type_id = models.AutoField(primary_key=True)
    phone_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'PhoneType'

    def __str__(self):
        return self.phone_type

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    pass_word = models.CharField(max_length=40)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'

    def __str__(self):
        return self.first_name + " " + self.last_name

class UserAddress(models.Model):
    user_address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    address_type = models.ForeignKey(AddressType, models.DO_NOTHING)
    address_1 = models.CharField(max_length=30, blank=True, null=True)
    address_2 = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    st = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserAddress'

    def __str__(self):
        return self.address_1

class UserInfo(models.Model):
    user_info_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    profile_bio = models.CharField(max_length=500, blank=True, null=True)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserInfo'

    def __str__(self):
        return self.profile_bio

class UserPhone(models.Model):
    user_phone_id = models.AutoField(primary_key=True)
    phone_type = models.ForeignKey(PhoneType, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserPhone'

    def __str__(self):
        return self.phone_number
