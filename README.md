# Projeto de listagem de entretenimentos/atividades

Essa aplicação salva os entretenimentos de um usuário para fins de organização.

## Instruções para usar esse projeto em sua máquina

1º) Clone o repositório com o seguinte comando

~~~
git clone https://github.com/NascimentoFrancisco/entertainment.git
~~~

2º) Abra em seu editor de preferência e crie e ative o virtualenv

### Windows:
>Criação
~~~
python -m venv venv
~~~
>Ativação
~~~
venv\Scripts\activate
~~~
### Linux:
>Criação
~~~
python3 -m venv venv
~~~
>Ativação
~~~
. venv/bin/activate
~~~

3º) Isntale as dependências:

~~~
pip install -r requirements.txt
~~~

4º) Faça as migrations e o migrate:

~~~
python manage.py makemigrations
~~~

~~~
python manage.py migrate
~~~

5º) Inicie o servidor e acesse o link:

~~~
python manage.py runserver
~~~

~~~
http://127.0.0.1:8000/
~~~
