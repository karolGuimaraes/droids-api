## Droids-API

### Configurando
 - Clonar o projeto: git clone https://github.com/karolGuimaraes/droids-api.git
 - Acesse a pasta /droids-api
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


- ` GET /demanda/<id> ` Retorna todas a demanda: 


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

- ` DELETE /excluir/<id> ` Excluir uma demanda: 


- ` PUT /finalizar/<id> ` Finalizar uma demanda: 




### Teste

Para executa os teste unitários: 

`$ docker-compose run app python manage.py test`

Resposta similar:

			Creating test database for alias 'default'...
			System check identified no issues (0 silenced).
			............
			----------------------------------------------------------------------
			Ran 12 tests in 0.062s


			OK
			Destroying test database for alias 'default'...






