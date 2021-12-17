# Bem vindo à Comunica Dev API

A ComunicaDev é uma plataforma de ensino do idioma inglês para programadores. Oferece também um programa completo de desenvolvimento de soft skills e habilidades de comunicação, orientação de carreira e outplacement no exterior

Toda a aplicação está contida dentro do diretório `app`.


`riquerements.txt` é uma coleção com todos os frameworks, microframeworks e bibliotecas necessárias para o uso da aplicação.

O diretório `migrations` contém a configuração necessária para a inicialização das tabelas no banco de dados.

**IMPORTANTE**: não esqueça de popular o arquivo `.env` com suas informações. Estando de acordo com o arquivo `.env.example`.


# 
## Iniciando
Após clonar o repostório e acessar em sua máquina local, entre em um ambiente virtual venv utilizando os comando abaixo.
##
Caso tenha alguma dúvida, você pode consultar a [documentação oficial](https://docs.python.org/3/library/venv.html).

    python -m venv venv --upgrade-deps

##

    source venv/bin/activate

## Instalando dependências
Para instalar as dependências do projeto utilize o comando abaixo

    pip install -r requirements.txt


## Iniciar tabelas
Para iniciar as tabelas no seu banco de dados utilize o comando abaixo

    flask db upgrade

## Run the app
Para rodar o servidor em sua máquia loca utilize o comando abaixo

    flask run


# Endpoints
Aqui está a documentação para utilização de todos os endpoints da aplicação:

    [ BASE URL: https://comunica-dev-api.herokuapp.com/api ]


- [Users](./documentation/users.md)
- [Address](./documentation/address.md)
- [Categories](./documentation/categories.md)
- [Leads](./documentation/leads.md)
- [lessons](./documentation/lessons.md)
- [captchas](./documentation/captchas.md)

