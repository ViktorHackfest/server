from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions

class MyUserDetailView(APIView):
    def post(self, request):
        return ""