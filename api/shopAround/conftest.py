import pytest
from django.core.management import call_command
from django.db.utils import OperationalError
from django.db import connections

@pytest.fixture(scope='function', autouse=True)
def seed_test_database():
    # for conn in connections.all():
    #     conn.close()

    # try:
    #     for conn in connections.all():
    #         with conn.cursor() as cursor:
    #             cursor.execute("SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = %s;", [conn.settings_dict['NAME']])
    #         conn.close()

        call_command('seed')

    # except OperationalError as e:
    #     print(f"Error during setup: {e}")

    # yield

    # for conn in connections.all():
    #     conn.close()
