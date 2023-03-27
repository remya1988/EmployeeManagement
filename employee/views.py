from django.shortcuts import render
from rest_framework import  generics
from .models import Employee,EmployeeLeave
from .serializer import  EmployeeSerializer,LoginSerializer,EmployeeEditSerializer,EmployeeDeleteSerializer,EmployeeDetailsSerializer,EmployeeSearchSerializer
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .permissions import IsAdmin
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from employLeave.serializer import EmployeeLeaveSerializer,EmployeeLeaveApprovalSerializer



# Create your views here.
class EmployeeListCreate(generics.ListCreateAPIView):
    search_fields = ['^emp_name','position','martial_status','job_title','work_location','reporting_to']
    filter_backends = (SearchFilter,)
    queryset=Employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_classes=(IsAdmin,)
    serializer_class = EmployeeSerializer


class LoginView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class = LoginSerializer
    def create(self,request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            uname=request.data['username']
            qs=User.objects.get(username=uname)
            print(uname)
            password=request.data['password']
            user=authenticate(username=uname,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser==1:
                    print(request.user.is_superuser)
                    return Response({"message":"Logged in as admins"})
                else:
                    logout(request)
                    return Response({"message":"Logged in as employee"})


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"Message":"Lgout successfully"})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_classes=(IsAdmin,)
    serializer_class = EmployeeDetailsSerializer

class EmployeeEditView(generics.UpdateAPIView):
    queryset=Employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_classes=(IsAdmin,)
    serializer_class = EmployeeEditSerializer

class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = (IsAdmin,)
    serializer_class = EmployeeDeleteSerializer

class SearchEmployeeView(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = (IsAdmin,)
    serializer_class = EmployeeSearchSerializer

class LeaveViewSearch(generics.ListCreateAPIView):
    search_fields = ['status']
    filter_backends = (SearchFilter,)
    queryset=EmployeeLeave.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_classes=(IsAdmin,)
    serializer_class = EmployeeLeaveSerializer

class LeaveApprovalView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeLeaveSerializer
    queryset=EmployeeLeave.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = (IsAdmin,)
    def create(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        leave=EmployeeLeave.objects.filter(user_id=id)
        serializer=EmployeeLeaveApprovalSerializer(instance=leave,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message : ":"Leave Approved..."})
        else:
            return Response(data=serializer.errors)



