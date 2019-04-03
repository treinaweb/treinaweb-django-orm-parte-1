from ..models import Endereco

def cadastrar_endereco(endereco):
    return Endereco.objects.create(rua=endereco.rua, numero=endereco.numero, complemento=endereco.complemento, bairro=endereco.bairro,
                            cidade=endereco.cidade, pais=endereco.pais)