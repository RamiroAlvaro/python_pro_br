import pytest
from model_mommy import mommy

from pypro.django_assertions import assert_equal
from pypro.modulos import facade
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return [mommy.make(Modulo, titulo=s) for s in 'Antes Depois'.split()]


def test_listar_modulos_ordenados(modulos):
    assert_equal(list(sorted(modulos, key=lambda modulo: modulo.titulo)), facade.listar_modulos_ordenados())
