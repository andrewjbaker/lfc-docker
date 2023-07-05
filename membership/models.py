from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from random import randint

# Create your models here.
# Source: https://www.codespeedy.com/extend-django-user-model-with-custom-fields/

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.create_membership_number()
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # Creates an ordinary user account for members
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)
    
    # Creates a superuser account with pre-defined extra field values
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be a staff'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be a superuser'
            )
        return (self._create_user(email, password, **extra_fields))
    

class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True, max_length=255, blank=False)
    membership_number = models.PositiveIntegerField('membership number', unique=True, blank=False)
    first_name = models.CharField('first name', max_length=50, blank=False)
    last_name = models.CharField('last name', max_length=50, blank=False)
    telephone = models.CharField('telephone', max_length=11, null=True, blank=False)
    address1 = models.CharField('address line 1', max_length=255, blank=False)
    address2 = models.CharField('address line 2', max_length=255, blank=True)
    city = models.CharField('city', max_length=255, blank=False)
    postcode = models.CharField('postcode', max_length=8, blank=False)
    is_staff = models.BooleanField('staff status',default=False)
    is_active = models.BooleanField('active',default=False)
    is_superuser = models.BooleanField('superuser',default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'telephone',
        'address1',
        'city',
        'postcode'
    ]

    objects = UserManager()

    def __str__(self):
        return str(self.membership_number)
    
    def address(self):
        return f"{self.address1}\n{self.addressline2}\n{self.city}\n{self.postcode}"
    
    def create_membership_number(self):
        unique_id = False

        # Creates a unique membership id by selecting a random 8 digit integer and checking if it exists
        while not unique_id:
            proposed_id = "%08d" % randint(00000000, 99999999)
            if not User.objects.filter(membership_number=proposed_id):
                unique_id = True
        
        self.membership_number = proposed_id

        return()