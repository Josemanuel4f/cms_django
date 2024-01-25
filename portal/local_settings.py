# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "django-insecure-5q_s786oyd@=kq^i(nnq3)*^#h0e@nx2ruo_2*8i!#l9y5kl+3"
NEVERCACHE_KEY = "%0&+x(d*jrg2l#9^vn*i#%*rl$4)75(+34%i61r5b%u*qnui02"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# Allowed development hosts
ALLOWED_HOSTS = ['*']
