from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

USER_TYPE = (
    ('buyer', 'Buyer'),
    ('seller', 'Seller'),
)


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, name, user_type, password=None):
        if not email:
            raise ValueError("Email address missing!")
        if not username:
            raise ValueError("Username missing!")
        if not name:
            raise ValueError("Name missing!")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
            user_type=user_type,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, name, user_type):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            name=name,
            user_type=user_type,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=120, unique=True)
    name = models.CharField(max_length=120)
    username = models.CharField(verbose_name="username", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=120, choices=USER_TYPE, default='buyer')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'user_type', 'name']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
