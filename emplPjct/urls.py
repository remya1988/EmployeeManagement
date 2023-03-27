"""emplPjct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from employee.views import LeaveApprovalView,LeaveViewSearch,EmployeeListCreate,EmployeeEditView,LogoutView,LoginView,EmployeeDeleteView,EmployeeDetailsView
from django.conf.urls import static
from django.conf import settings
from knox import views as knox_views
from employLeave.views import EmployeeLeaveApplyView,EmployeeLeaveListView
router =  DefaultRouter()

#API for employee to create their leave applications Only employee can access this
router.register("api/employee/leave", EmployeeLeaveApplyView, basename="leave"),


urlpatterns = [
    path('admin/', admin.site.urls),

    # Api's for ADMIN to create edit,view,delete employees Only Admin can access this
    path('api/empl/',EmployeeListCreate.as_view(),name="add-empl"),
    path('api/empl/edit/<int:pk>/',EmployeeEditView.as_view(),name="edit"),
    path('api/empl/delete/<int:pk>/',EmployeeDeleteView.as_view(),name="delete"),
    path('api/empl/details/<int:pk>/',EmployeeDetailsView.as_view(),name="details"),

    #API's for ADMIN to search and edit employee leave applications Only Admin can access this
    path('api/empl/leave-search/',LeaveViewSearch.as_view(),name="search-leave"),
    path('api/empl/leave-approve/<int:pk>', LeaveApprovalView.as_view(), name="approval"),

    # API for empoyee to view their leave applications Only employee can access this
    path('api/employee/leave-view/',EmployeeLeaveListView.as_view(),name="leave-view"),

    #API for login and logout This api's have access to both Employees and Admin
    path('api/login', TokenObtainPairView.as_view()),
    path('api/logout', LogoutView.as_view(),name="logout"),
    path('api/refresh', TokenRefreshView.as_view()),

]+router.urls

