
from django.contrib import admin
from .models import Todo
 
@admin.register(Todo)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Todo._meta.get_fields()]