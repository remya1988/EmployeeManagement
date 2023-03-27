from django.shortcuts import render
from employee.models import Employee,EmployeeLeave
from rest_framework import  generics
from django.contrib.auth.models import Permission
from rest_framework import authentication,permissions
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from django.http.response import JsonResponse
from .serializer import EmployeeLeaveSerializer,EmployeeLeaveViewSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework import status
# Create your views here.

# View to apply leave application for employee
class EmployeeLeaveApplyView(ModelViewSet):
    serializer_class = EmployeeLeaveSerializer
    queryset = EmployeeLeave.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes=(IsEmployee)
    def create(self,request,*args,**kwargs):
        user=request.user
        print(user.id)
        if user.is_superuser == 0:
            serializer=EmployeeLeaveSerializer(data=request.data,context={"user":user})
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        else:
            return Response({"message":"Only Employee can use this page"})


# View to list all the leaves aplied by login employee
class EmployeeLeaveListView(APIView):
    def get(self, request, format=None):
        search_fields = ['status']
        filter_backends = (SearchFilter,)
        user=request.user
        qs = EmployeeLeave.objects.filter(user_id=user.id)
        serializer = EmployeeLeaveViewSerializer(qs,many=True)
        # lst=[item for item in qs]
        return Response(data=serializer.data)

