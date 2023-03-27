from rest_framework import serializers
from employee.models import Employee,EmployeeLeave
from django.contrib.auth.models import User

class EmployeeLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLeave
        exclude = ["user"]

    def create(self, validated_data):
        user=self.context.get("user")
        return EmployeeLeave.objects.create(**validated_data,user=user)
    # def get(self):
    #     user=self.context.get("user")
    #     return EmployeeLeave.objects.get(user_id=user.id)

class EmployeeLeaveViewSerializer(serializers.ModelSerializer):
    # id=serializers.CharField(read_only=True)
    # nature_of_leave=serializers.CharField(read_only=True)
    # status=serializers.CharField(read_only=True)
    # apply_date=serializers.CharField(read_only=True)
    class Meta:
        model = EmployeeLeave

        exclude=["user","id"]


class EmployeeLeaveApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeLeave
        fields=["status"]