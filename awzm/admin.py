from django.contrib import admin

from .models import Foo, Bar


@admin.register(Foo)
class FooAdmin(admin.ModelAdmin):
    pass


@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    pass
