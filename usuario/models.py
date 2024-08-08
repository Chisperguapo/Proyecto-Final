from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin # Are used for management personalized users.
from django.utils import timezone # to handle dates and times sensitively in time zone

class CustomUserManager(UserManager): # La creación de la clase'CustomUserManager' hereda de la clase'UserManager'.
    def _create_user(self,last_name, birth_date, direction, cell, email, password, **extra_fields): # Se crea un 'metodo interno' para crear un usuario con los campos que se mecesiten.
        if not email:
            raise ValueError("You have not provided a valid e-mail addres.")
        
        email =  self.normalize_email(email) # Normaliza el 'email'
        user = self.model(last_name=last_name, birth_date=birth_date, direction=direction, cell=cell, email=email, **extra_fields) # Se especifican los 'campos' al 'modelo'
        user.set_password(password) # Cambia el contenido de la 'contraseña' en el 'modelo'.
        user.save(using=self._db) # Se guarda el 'usuario' en la 'base de datos'.

        return user
    
    def _create_superuser(self, email, password, **extra_fields): # Se crea un 'metodo interno' para crear un usuario con los campos que se mecesiten.
        if not email:
            raise ValueError("You have not provided a valid e-mail addres.")
        
        email =  self.normalize_email(email) # Normaliza el 'email'
        user = self.model(email=email, **extra_fields) # Se especifican los 'campos' al 'modelo'
        user.set_password(password) # Cambia el contenido de la 'contraseña' en el 'modelo'.
        user.save(using=self._db) # Se guarda el 'usuario' en la 'base de datos'.

        return user


    
    def create_user(self,  last_name=None, birth_date=None, direction=None, cell=None, email=None, password=None, **extra_fields): # Se crea un 'metodo estandar'.
        extra_fields.setdefault('is_staff', False) # Se llama a _create_user con is_staff e is_superuser configurados en False.
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(last_name, birth_date, direction, cell, email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields): # Metodo público para crear un 'super usuario'.
        extra_fields.setdefault('is_staff', True) # Llama a '_create_user' con is_staff e is_superuser configurados en True.
        extra_fields.setdefault('is_superuser', True)
        return self._create_superuser(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin): # Se definirá el modelo de 'Usuario' que hereda de 'AbstractBaseUser' y 'PermissionMixin' para permisos.
    name = models.CharField(max_length=100, blank=True, null=True, default='')# Campos que se rellenarán.
    last_name = models.CharField(max_length=120, blank=True, default='')
    birth_date = models.DateField(blank=True, null=True)
    direction = models.CharField(max_length=150, blank=True, default='')
    cell = models.CharField(max_length=15, blank=True, default='')
    email = models.EmailField(blank=True, default='', unique=True) 

    is_active = models.BooleanField(default=True) # Se hace uso del 'PermissionsMixin' y se le asigna un estado 'activo' por 'defecto'. 
    is_superuser = models.BooleanField(default=False) # Se les asiga por defecto que no son 'superusuarios'.
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now) # Se muestra la fecha de primera entrada.
    last_login = models.DateTimeField(blank=True, null=True) # Se muestra la ultima fecha de 'login'.

    objects = CustomUserManager() # Se hace uso de clase creada para gestionar la creación de usurios.

    # Se configura los campos del inicio de sesión y otros ajustes.
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta: # Meta datos del modelo.
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self): # Se muestra el nombre completo del usuario.
            return self.name
        
    def get_short_name(self): # Se muestra el nombre corto del usuario.
            return self.name or self.email.split('@')[0]
    
    def get_id(self):
        return self.id                                                  