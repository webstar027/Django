from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "full_name", "timestamp", "updated"]
    form = SignUpForm
    class Meta:
        modal = SignUp
        fields = ['full_name', 'email']
        exclude = ['full_name']

admin.site.register(SignUp, SignUpAdmin)