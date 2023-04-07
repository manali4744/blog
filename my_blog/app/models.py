from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import EmailValidator, RegexValidator


class UserManager(BaseUserManager):
    def create_user(self,email, name, password=None, password2=None):

        user = self.model(
            email=self.normalize_email(email),
            name=name

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, name, password=None):
        user = self.create_user(
            email,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_valid = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[EmailValidator]
    )
    name = models.CharField(max_length=250, validators=[RegexValidator(regex='^[A-Za-z]{2,25}$', message="invalid name")])
   
    
    gender_choice = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    gender = models.CharField(null=True,blank=True,choices=gender_choice,max_length=7)
    is_active = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    def get_all_permissions(self, user=None):
        if self.is_admin:
            return set()

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

class Blogger(models.Model):
    blogger = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.blogger.email
    