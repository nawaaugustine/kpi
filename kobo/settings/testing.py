# coding: utf-8
from mongomock import MongoClient as MockMongoClient

from .base import *

# For tests, don't use KoBoCAT's DB
DATABASES = {
    'default': env.db_url(
        'KPI_DATABASE_URL' if 'KPI_DATABASE_URL' in os.environ else 'DATABASE_URL',
        default='sqlite:///%s/db.sqlite3' % BASE_DIR
    ),
}

DATABASE_ROUTERS = ['kpi.db_routers.TestingDatabaseRouter']

TESTING = True

# Decrease prod value to speed-up tests
SUBMISSION_LIST_LIMIT = 100

ENV = 'testing'

# Run all Celery tasks synchronously during testing
CELERY_TASK_ALWAYS_EAGER = True


MONGO_CONNECTION_URL = 'mongodb://fakehost/formhub_test'
mongo_client = MockMongoClient(
    MONGO_CONNECTION_URL, connect=False, journal=True, tz_aware=True)
MONGO_DB = mongo_client['formhub_test']

ENKETO_URL = 'http://enketo.mock'
ENKETO_INTERNAL_URL = 'http://enketo.mock'

# Do not use cache with Constance in tests to avoid overwriting production
# cached values
CONSTANCE_DATABASE_CACHE_BACKEND = None
INSTALLED_APPS += ('djstripe', "kobo.apps.stripe")
STRIPE_ENABLED = True
