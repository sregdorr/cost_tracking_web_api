

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9n@a8^v%a$-q$j!b&nk_q68p627ga%r7vb4y512ak%)sv))&rg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cost-tracking',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}