import pytest

from estacionamento_estagiario import calcular_tarifa


@pytest.mark.parametrize(
	"minutos, esperado",
	[
		(0, 0.00), (1, 0.00), (15, 0.00), (16, 12.00),
		(180, 12.00), (181, 15.00), (240, 15.00), (241, 18.00),
		(300, 18.00), (301, 21.00), (719, 39.00), (720, 39.00),
		(721, 60.00), (1000, 60.00),
	],
)
def test_tarifa_estagiario(minutos, esperado):
	assert calcular_tarifa(minutos) == esperado


@pytest.mark.parametrize("minutos", [-1, -60])
def test_tempo_negativo(minutos):
	with pytest.raises(ValueError):
		calcular_tarifa(minutos)


@pytest.mark.parametrize("minutos", [None, 15.0, "15"])
def test_tempo_nao_inteiro(minutos):
	with pytest.raises(TypeError):
		calcular_tarifa(minutos)
