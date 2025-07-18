from django.db import models

class Foo(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class Bar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
