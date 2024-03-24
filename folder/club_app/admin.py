from django.contrib import admin
# Register your models here.
from .models import Student, Role, Department


admin.site.register(Student)
admin.site.register(Role)
admin.site.register(Department)