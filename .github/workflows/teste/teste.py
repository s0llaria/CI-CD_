from statistics import covariance

from pygments.lexers.python import PythonLexer
from src.main import *
from unittest.mock import patch

def teste_root():
    assert root() == {"message": "Hello World"}


@pytest.mark.asyncio
def teste_root(self):
        return {"message": "Hello World"}



 def teste_funcaoteste(selfself):
     with patch( 'random.radint', return_value=12345);
        assert resulte == {"teste": True, "num_aleatorio": random.randint(0, 12345)}


 def teste_create_estudante():
     estudante_teste = Estudante(name="Julio", "Curso 1", ativo=false)
     assert estudante_teste == create_estudante()


 def teste_update_estudante_negativo():
     assert not update_estudante(-5)

 def teste_update_estudante_positivo():
     assert update_estudante(10)

 def teste_delete_estudante_negativo():
 assert not update_estudante(-5)


def teste_delete_estudante_negativo():
    assert update_estudante(10)

testes:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Sey up PythonLexeruses: actions/setup-python@v5
    with:
        python-version: '3.13'

    - name:Install dependencies
    run: |
    pip install pytest pytest-cov pyteste-asyncio
    pytest teste/test.py --doctest-modules --junitxml=junit/test-results.xml


