import pytest
from django.urls import reverse

from pypro.django_assertions import assert_equal


@pytest.fixture
def resp(client, db):
    return client.get(reverse('turmas:indice'))


def test_status_code(resp):
    assert_equal(resp.status_code, 200)
