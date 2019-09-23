from django.test import TestCase, Client
from droid_api.models import *
from rest_framework import status
import json


class Teste(TestCase):
    def setUp(self):
        conta = Conta.objects.create(username = 'user1', first_name = 'user', email = 'user1@gmail.com')
        endereco = Endereco.objects.create(cep='00000000', logradouro='Rua b', numero='1', bairro='Guaratiba', cidade='Rio de janeiro', estado='Rio de janeiro')
        peca = Peca.objects.create(descricao='Teclado')
        Demanda.objects.create(peca=peca, endereco_entrega=endereco, anunciante=conta) 
    
    
    def teste_criar(self):
        data = {
            'anunciante': 'user1', 
            'peca': { 
                'descricao': 'Cabo' 
            } , 
            'endereco_entrega': { 
                'cep': '00000000', 
                'logradouro':'Rua b', 
                'numero': '1', 
                'bairro': 'Guaratiba', 
                'cidade': 'Rio de janeiro', 
                'estado': 'Rio de janeiro' 
            }
        }
        response = self.client.post('/adicionar', json.dumps(data), content_type="application/json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def teste_criar_sem_anunciante(self):
        data = {
            'anunciante': 'user2', 
            'peca': { 
                'descricao': 'Cabo' 
            } , 
            'endereco_entrega': { 
                'cep': '00000000', 
                'logradouro':'Rua b', 
                'numero': '1', 
                'bairro': 'Guaratiba', 
                'cidade': 'Rio de janeiro', 
                'estado': 'Rio de janeiro' 
            }
        }
        response = self.client.post('/adicionar', json.dumps(data), content_type="application/json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def teste_criar_campo_nulo(self):
        data = {
            'anunciante': 'user1', 
            'peca': { 
                'descricao': '' 
            } , 
            'endereco_entrega': { 
                'cep': '00000000', 
                'logradouro':'Rua b', 
                'numero': '1', 
                'bairro': 'Guaratiba', 
                'cidade': 'Rio de janeiro', 
                'estado': 'Rio de janeiro' 
            }
        }
        response = self.client.post('/adicionar', json.dumps(data), content_type="application/json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)


    def teste_buscar(self):
        response = self.client.get('/demanda/1')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    
    def teste_buscar_sem_demanda(self):
        response = self.client.get('/demanda/10000')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


    def teste_editar(self):
        data = {
            'demanda': '1', 
            'peca':{ 
                'descricao': 'Teclado'
            } , 
            'endereco_entrega':{ 
                'cep': '00000000', 
                'logradouro':'Rua b', 
                'numero': '1', 
                'bairro': 'Guaratiba', 
                'cidade': 'Rio de janeiro', 
                'estado': 'Rio de janeiro' 
            }
        }
        response = self.client.put('/editar', json.dumps(data), content_type="application/json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def teste_editar_sem_demanda(self):
        data = {
            'demanda': '10000', 
            'peca':{ 
                'descricao': 'Teclado'
            } , 
            'endereco_entrega':{ 
                'cep': '00000000', 
                'logradouro':'Rua b', 
                'numero': '1', 
                'bairro': 'Guaratiba', 
                'cidade': 'Rio de janeiro', 
                'estado': 'Rio de janeiro' 
            }
        }
        response = self.client.put('/editar', json.dumps(data), content_type="application/json")
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


    def teste_editar_campo_nulo(self):
        data = {
            'demanda': '1', 
            'peca':{ 
                'descricao': 'Teclado'
            } , 
        }
        response = self.client.put('/editar', json.dumps(data), content_type="application/json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)



    def teste_finalizar(self):
        response = Client().put('/finalizar/1')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def teste_finalizar_sem_demanda(self):
        response = self.client.put('/finalizar/10000')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)



    def teste_excluir(self):
        response = self.client.delete('/excluir/1')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def teste_excluir_sem_demanda(self):
        response = self.client.delete('/excluir/10000')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
