import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains, assert_equal
from pypro.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def resp(client, modulo):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_title(resp):
    assert_contains(resp, '<title>Python Pro - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'<a class="navbar-brand" href="{reverse("base:home")}">Python Pro</a>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"')
