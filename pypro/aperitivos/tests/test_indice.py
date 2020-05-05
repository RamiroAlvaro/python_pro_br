import pytest
from django.urls import reverse

from pypro.django_assertions import assert_equal, assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


@pytest.mark.parametrize(
    'titulo',
    [
        'Video Aperitivo: Motivação',
        'Instalação Windows'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'slug',
    [
        'motivacao',
        'instalacao-windows'
    ]
)
def test_link_video(resp, slug):
    link_video = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{link_video}"')
