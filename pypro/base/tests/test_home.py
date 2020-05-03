import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains, assert_equal


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_title(resp):
    assert_contains(resp, '<title>Python Pro</title>')


def test_home_link(resp):
    assert_contains(resp, f'<a class="navbar-brand" href="{reverse("base:home")}">Python Pro</a>')
