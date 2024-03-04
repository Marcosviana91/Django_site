# EBAC - Django
- Instalar o Django \
`pip install Django`
- Iniciar um projeto \
`django-admin startproject mysite` ou \
`python3 -m django startproject mysite` \
Isso irá criar uma pasta chamada *mysite* `cd mysite/`
`python manage.py startapp blog`
Dentro da pasta *mysite* há outra pasta chamada *mysite*, que é onde ficam os arquivos de configuração do projeto. \
São ele:
-  **\_\_init__.py** - indica ao Python que o diretório é um pacote. Ele é executado ao importar o pacote.
- **settings.py** - Contém as definiçoes de configuração para o projeto Django.
- **urls.py** - Contém padrões de URL para o projeto.
- **wsgi.py** e **asgi.py**- Basicamente um script Python para ajudar a executar o servidor de desenvolvimento e impantar o projeto em ambiente de produção (**w**eb e **a**ssíncrono).
- **manage.py** - ultilitário para interagir com o projeto.
