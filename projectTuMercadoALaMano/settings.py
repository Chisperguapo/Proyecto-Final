from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


STATICFILES_DIRS=['C:/projectTuMercadoALaMano/productos/static/productos', 'C:/projectTuMercadoALaMano/contacto/static/contacto']
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1(qox*%1%0bpm+pcs)4$c!9d!d69$=%%$p%7ag*4*^v(9e&wo!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '46ae-190-131-210-13.ngrok-free.app']

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos',
    'tienda',
    'carro',
    'usuario.apps.UsuarioConfig',
    'contacto.apps.ContactoConfig', # Se especifica la ruta de la app'contacto' en el archivo apps.py'apps' con la clase creada'ContactoConfig'.
    'crispy_forms', # Se agrega la aplicación para los formularios crispy'crispy_forms'.
    'crispy_bootstrap5', # Se agrega la aplicación de crispy que conttienen el bootstrap5'crispy_bootstrap5'.
    'appAdmin',
    'reportes',
    'paypal.standard.ipn', # Aplicación paypal para la pasarela de pago.
    'pasarelaPago',

    
]   

# Agregamos la configuración correspondiente para que funcioné el crispy:
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

#
AUTH_USER_MODEL = 'usuario.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projectTuMercadoALaMano.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                'C:/projectTuMercadoALaMano/tienda/templates/tienda', 
                'C:/projectTuMercadoALaMano/productos/templates/productos',
                'C:/projectTuMercadoALaMano/carro/templates/carro', 
                'C:/projectTuMercadoALaMano/usuario/templates/usuario',
                'C:/projectTuMercadoALaMano/reportes/templates/reportes', 
                'C:/projectTuMercadoALaMano/appAdmin/templates/admin',
                'C:/projectTuMercadoALaMano/pasarelaPago/templates',
                ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carro.context_processor.importe_total_carro',
            ],
        },
    },
]

WSGI_APPLICATION = 'projectTuMercadoALaMano.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tuMercadoALaMano',
        'USER': 'webstore',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}


# Se le indica al programa que va incluir un modelo de tabla de usuario diferente al predefinido:
# AUTH_USER_MODEL = 'usuario.Usuario'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL='/media/'
MEDIA_ROOT='C:/projectTuMercadoALaMano/productos/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Recipiente para el correo:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'webstorewarriors@gmail.com'
EMAIL_HOST_PASSWORD = 'h g a l s l d g s j s o k a q i' #Constraseña de la aplicación


# Tiempo de expiración del token en segundos (default: 3 días)
PASSWORD_RESET_TIMEOUT = 60 * 60 * 24 * 3  # 3 días


# configuración para la librería 'Messages':
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Configuración correo paypal
PAYPAL_RECEIVER_EMAIL = 'sb-aot0030968188@business.example.com'
PAYPAL_TEST = True 

# settings.py
PAYPAL_CLIENT_ID = 'Af7jwCOFjz5MtO_imp-z_1t1Gr8xRoQAdVaizBjw3BpJM9qO8k5oYGxIU0EB8T-tTbKpsBD6dCsnpcmE'
PAYPAL_CLIENT_SECRET = 'ECCeX4KUzBC45HizfZHxg113PY10gsKQbJciCVC1DAvs52gOu5BGNFahz1dYq6CAtx9t1w4kdSJOBh53'
PAYPAL_MODE = 'sandbox'  # o 'live' si estás en producción
