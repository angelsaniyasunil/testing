from django import forms 
from . models import ProductModel,RegisterModel
import re


class ProductAddingForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"

class RegisterViewForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
         model = RegisterModel
         fields = "__all__"
         
#     def clean_full_name(self):
#         full_name = self.cleaned_data["full_name"]
#         if len(full_name)

#     def clean_email(self):
#         email = self.cleaned_data["email"]

#         if RegisterModel.objects.filter(email=email).exists():
#             raise forms.ValidationError("Email already exists")
#         return email

#     def clean_password(self):
#         password = self.cleaned_data["password"]
#         if len(password) <8:
#             raise forms.ValidationError("Password must contain atleast 8 char")
#         if not re.search(r'[A-Z]', password):
#             raise forms.ValidationError("Password must contain atleast one uppercase")
#         if not re.search(r'[a-z]', password):
#             raise forms.ValidationError("Password must contain atleast one lowercase")
#         if not re.search(r'[0-9]', password):
#                     raise forms.ValidationError("Password must contain atleast one number")
#         if not re.search(r'[@#$%^&*()/]', password):
#                     raise forms.ValidationError("Password must contain atleast one special character")

#         return password

#         def clean(self):
#             data = super().clean()
#             password = data.get("password")
#             confirm_password = data.get("confirm_password")
#             if password and confirm_password:
#                 if password != confirm_password:
#                     self.add_error("confirm_password","Password and confirm password mismatch")
#             return data
            