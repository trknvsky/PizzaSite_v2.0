# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.models import User, Group


class UserAdmin(admin.ModelAdmin):

    class Meta:
        model = User
