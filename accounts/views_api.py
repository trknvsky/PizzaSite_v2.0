from django.views.generic.base import View
from django.shortcuts import render, redirect, render_to_response
from django.http import JsonResponse
from accounts.models import User


class UserApiView(View):

    def get(self, request):
        print('Get api request')
        users = User.objects.all()
        serialized_users = []
        for user in users:
            serialized_users.append(user.get_serialize_data())
        return JsonResponse({'users_list': serialized_users})


class CreateUserApiView(View):

    def get(self, request):
        return JsonResponse({"message": "Method not supported"})

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create(email=email, password=password)
        serialized_users = []
        for user in users:
            serialized_users.append(user.get_serialize_data())
            return JsonResponse({'users_list': serialized_users})
