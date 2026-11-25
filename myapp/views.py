from django.shortcuts import render,get_object_or_404
from . models import RegisterModel,Student
from . models import ProductModel
from . forms import ProductAddingForm,RegisterViewForm

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from.serializer import StudentSerializer
from rest_framework import status
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request, "contact.html")

def product(request):
    return render(request, "product.html")

def register(request):
    if request.method == "FILES":
        image = request.POST.get("profile")
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        number = request.POST.get("number")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        mydata = RegisterModel(
            profile = image,
            full_name = full_name,
            username = username,
            number = number,
            gender = gender,
            dob = dob,
            email = email,
            password = password
        )
        mydata.save()
        print("saved")

    return render(request, "register.html")

def dashboard(request):
    values = [1,2,3,4,5,6,7,8,9,10]
    mydata = RegisterModel.objects.all()
    return render(request, "dashboard.html", {"data":values, "mydata":mydata})

def login_view(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")

        data = RegisterModel.objects.filter(username=name).first()
        if data and data.password == password:
            request.session["username"]=data.username
            request.session["fullname"]=data.full_name
            request.session["email"]=data.email


def product(request):
    if request.method == "POST":
        data = ProductAddingForm(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            print("saved")
        return render(request,"product.html")


def register_view(request):
    if request.method == "POST":
        form = RegisterViewForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("saved")

                
            subject = "Registration Successful"
            message = f"""
                    Hello{form.full_name}
                    Your registration has been completed successfully,

                    Thankyou,
                    """
            send_mail(subject,messsage,
                        settings.DEFAULT_FROM_EMAIL,form.email,fail_silently=False)
            messages.success(request,"Registration Successful")

    else:
        form = RegisterViewForm()
    return render(request,"register_view.html",{"form":form})




def update_list(request,jk):
    form = RegisterModel.objects.get(id = jk)
    return render(request,"update_list.html",{"data":form})

# def update_list(request, jk):
#     user = get_object_or_404(RegisterModel, id=jk)
# if request.method =="POST":
#     form = updateform(request.POSt , instance = user)
#     if form.is_valid():
#         form.save()
#         return redirect("dashboard")
#     else:
#         form = UpdateForm(instance=user)
#     return render(request, "update_list.html",{"data":form})

class StudentList(APIView):
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        student = student.object.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)

class StudentDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(Student, id=id)

    def get(self, request, id):
        stud = self.get_object(id)
        serializer = StudentSerializer(stud)
        return Response(serializer.data)

    def put(self, request, id):
        stud = self.get_object(id)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
            stud = self.get_object(id)
            serializer = StudentSerializer(stud, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        stud = StudentDetail.object.get(id=id)
        stud.delete()
        return Response({"message":"Student deleted"}, status=status.HTTP_200_OK)



    
