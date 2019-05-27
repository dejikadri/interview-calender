from django.db import models
import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class AuthUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Custom user to allow email as username
        """
        if not email:
            raise ValueError("Email is required")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    jwt_secret = models.UUIDField(default=uuid.uuid4)

    objects = AuthUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


def jwt_get_secret_key(user_model):
    return user_model.jwt_secret
