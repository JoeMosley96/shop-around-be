import pytest
from django.core.management import call_command

@pytest.fixture(scope='function', autouse=True)
def seed_test_database():
    call_command('flush','--no-input')
    call_command('seed','--no-input')

