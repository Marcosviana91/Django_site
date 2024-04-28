`python manage.py createsuperuser`
user
31169111

`python manage.py shell`
```python
# Filter retorna uma lista
user = User.objects.filter()   
# Get retorna um item apenas
user = User.objects.get(username='user')
```