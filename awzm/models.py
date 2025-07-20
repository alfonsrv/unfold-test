from django.db import models

class Foo(models.Model):
    number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


class Bar(models.Model):
    class Choices(models.IntegerChoices):
        ONE = 1, 'One'
        TWO = 2, 'Two'

    number = models.IntegerField(
        choices=Choices.choices,
    )
    foo = models.ForeignKey(
        'awzm.Foo',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=12
    )  # just here to help trigger validation failure
    created = models.DateTimeField(auto_now_add=True)
