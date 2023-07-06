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
    """A class to define a user for the membership system (i.e. a member)
    
    :param AbstractBaseUser: An abstract base class on which to build a custom user model
    :type AbstractBaseUser: `AbstractBaseUser` class
    :param PermissionsMixin: Class which adds the fields and methods necessary to support the Group and Permission models using the ModelBackend
    :type PermissionsMixin: `PermissionsMixin` class
    :param email: The email address of the user and the primary key for the member account
    :type email: `str`
    :param membership_number: A randomly generated eight digit integer for the member id
    :type membership_number: `int`
    :param first_name: The member's first name
    :type first_name: `str`
    :param last_name: The member's last name
    :type last_name: `str`
    :param telephone: The contact telephone number for the member
    :type telephone: `str`
    :param address1: The first line of the member's address
    :type address1: `str`
    :param address2: The second line of the member's address
    :type address2: `str`, optional
    :param city: The city in which the member resides
    :type city: `str`
    :param postcode: The postcode of the member's address
    :type postcode: `str`
    :param is_staff: Determines whether the account belongs to a staff member, defaults to False
    :type is_staff: `bool`
    :param is_active: Determines whether the account is active, defaults to False
    :type is_active: `bool`
    :param is_superuser: Determines whether the account belongs to an administrator, defaults to False
    :type is_superuser: `bool`

    """

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
        """Returns a string representation of a `User` account
        
        :param self: An object of the User class i.e. a member account
        :type self: `User`
        :return: The string representation of the member account i.e. their membership number
        :rtype: `int`
        """
        return str(self.membership_number)
    
    def address(self):
        """Returns a string representation of the member's address
        
        :param self: An object of the User class i.e. a member account
        :type self: `User`
        :return: A concatenated output of the address including both lines, city and postcode
        :rtype: `str`
        """
        return f"{self.address1}\n{self.addressline2}\n{self.city}\n{self.postcode}"
    
    def create_membership_number(self):
        """Creates a unique eight-digit identifier for the member's id and assigns it to the member
        
        :param self: An object of the User class i.e. a member account
        :type self: `User`
        """
        unique_id = False

        # Creates a unique membership id by selecting a random 8 digit integer and checking if it exists
        while not unique_id:
            proposed_id = "%08d" % randint(00000000, 99999999)
            if not User.objects.filter(membership_number=proposed_id):
                unique_id = True
        
        self.membership_number = proposed_id

        return()