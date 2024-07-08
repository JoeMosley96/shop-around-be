import pytest
from django.core.management import call_command
from django.db.utils import OperationalError
from django.db import connections

@pytest.fixture(scope='function', autouse=True)
def seed_test_database():
    for conn in connections.all():
        conn.close()

    try:    
        call_command('seed')

    except OperationalError as e:
        print(f"Eroor during setup: {e}")

    yield

    for conn in connections.all():
        conn.close()
