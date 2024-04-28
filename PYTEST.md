# Instalando dependências
<!-- `pip install pytest==5.4.0`  \ -->
`pip install pytest==6.2.5`  \
`pip install pytest-django==4.4.0`  \
`pip install Faker==8.11.0`  \
`pip install factory_boy==3.2.0`


mysite/tests/models/test_post.py
```Python
import pytest

from blog.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')


@pytest.mark.djando_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'

```

mysite/pytest.ini

```
[pytest]
DJANGO_SETTINGS_MODULE = mysite.settings
python_files = tests.py test_*.py *_tests.py
```

`pytest`