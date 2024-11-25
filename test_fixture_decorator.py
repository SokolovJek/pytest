from _pytest.fixtures import SubRequest
import pytest
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from pytest import SubRequest


@pytest.fixture(scope="module")
def resource_setup(request: SubRequest):
    print(type(request))
    print(f'resource start {type(request)}')
    def request_teardown():
        print(f'resource teardown')
    request.addfinalizer(request_teardown)
    return "http://localhost:2222"

def test_1(resource_setup):
    print(f'test_1 run, do connect to {resource_setup}')

def test_2(resource_setup):
    print(f'test_2 run, do connect to {resource_setup}')

def test_3(resource_setup):
    print(f'test_3 run, do connect to {resource_setup}')
