import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_equal, assert_contains


@pytest.fixture
def videos(db):
    return mommy.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_link_aperitivos_in_navbar(resp):
    link_aperitivos = reverse('aperitivos:indice')
    assert_contains(resp, f'<a class="nav-link" href="{link_aperitivos}">Aperitivos</a>')


def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_link_video(resp, videos):
    for video in videos:
        link_video = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{link_video}"')
