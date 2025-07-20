from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.admin import TabularInline as UnfoldTabularInline

from .models import Foo, Bar


class BarInline(UnfoldTabularInline):
    model = Bar
    extra = 1


@admin.register(Foo)
class FooAdmin(UnfoldModelAdmin):
    inlines = [
        BarInline
    ]


@admin.register(Bar)
class BarAdmin(UnfoldModelAdmin):
    pass
