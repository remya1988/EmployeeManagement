from rest_framework import serializers
from .models import Employee,EmployeeLeave
from django.contrib.auth.models import User
from django.core.mail import send_mail

class EmployeeSerializer(serializers.ModelSerializer):
    prof_pic = serializers.ImageField(max_length=None,use_url=True)
    # first_name="Inserted"
    class Meta:
        model = Employee
        exclude = ["user"]

    def create(self, validated_data):

        email = self.validated_data.get('email')
        print(email)
        password = self.validated_data.get('password')
        emp_name = self.validated_data.get('emp_name')
        user = User.objects.create_user(first_name=emp_name, email=email, username=email, password=password)
        # user=User.objects.create(**validated_data)
        ph_no = self.validated_data.get('ph_no')
        emergency_no = self.validated_data.get('emergency_no')
        address = self.validated_data.get('address')
        position = self.validated_data.get('position')
        dob = self.validated_data.get('dob')
        martial_status = self.validated_data.get('martial_status')
        blood_gp = self.validated_data.get('blood_gp')
        job_title = self.validated_data.get('job_title')
        work_location = self.validated_data.get('work_location')
        date_join = self.validated_data.get('date_join')
        reporting_to = self.validated_data.get('reporting_to')
        linkedin = self.validated_data.get('linkedin')
        prof_pic = self.validated_data.get('prof_pic')

        emp = Employee.objects.create(emp_name=emp_name, ph_no=ph_no, emergency_no=emergency_no, address=address,
                                      position=position, dob=dob,
                                      martial_status=martial_status, blood_gp=blood_gp, job_title=job_title,
                                      work_location=work_location,
                                      date_join=date_join, reporting_to=reporting_to, linkedin=linkedin,
                                      prof_pic=prof_pic, email=email, password=password,
                                      user=user)
        emp.save()
        send_mail(
            "Employee:Employee Portal",
            f"Your username is  {email} and password is {password}",
            "remyapillai1988@gmail.com",
            [email]
        )
        # Employee.objects.create(user=user,**emp_data)
        return emp

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)

class EmployeeEditSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

class EmployeeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

class EmployeeSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

