## Droids-API

### Configurando
 - Clonar o projeto: git clone https://github.com/karolGuimaraes/challenge-bravo.git
 - Acesse a pasta /droids
 - Executar:  `$ docker-compose up`
 
 
### Funcionamento

Acessando ( http://localhost:8000/ ), onde:

- ` POST /usuario `  Criar um usuário (Administrador ou Anunciante):
	 Criar um usuário para adicionar uma demanda.
	 Se o 'admin' for sim, o usuário é marcado como Administrador.
	 O username é único.

	- Envio:
		{ 
			"telefone": "000000000", 
			"username":"user_test", 
			"first_name":"test", 
			"email": "user.silva@gmail.com", 
			"password": 12345, 
			"admin": "Sim"
		}



- ` GET /demandas ` Retorna todas as demandas: 


- ` POST /adicionar ` Adicionar uma demanda:

	- Envio:
			{
			 	"anunciante": "username", 
			 	"peca": { 
					"descricao": "Memória" 
				} , 
			  	"endereco_entrega": { 
					"cep": "00000000", 
					"logradouro": "Rua b", 
					"numero":"1", 
					"bairro":"Guaratiba", 
					"cidade": "Rio de janeiro", 
					"estado": "Rio de janeiro" 
				} 
			}



- ` PUT /editar ` Editar uma demanda:

	- Envio:
		{
			"demanda": "2", 
			"peca": { 
				"descricao": "Memória" 
			} , 
			"endereco_entrega": { 
				"cep": "00000000", 
				"logradouro": "Rua b", 
				"numero":"1", 
				"bairro":"Guaratiba", 
				"cidade": "Rio de janeiro", 
				"estado": "Rio de janeiro" 
			} 
		}

- ` DELETE /excluir ` Excluir uma demanda: 

	- Envio:
		{ "id": 2 }


- ` PUT /finalizar ` Finalizar uma demanda: 

	- Envio:
		{ "id": 2 }



### Teste

Para executa os teste unitários: 

`$ docker-compose run app python manage.py test`

Resposta similar:




