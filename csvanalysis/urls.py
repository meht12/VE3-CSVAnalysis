from django.urls import path,include
from .views import *

urlpatterns = [
      path('upload/', upload_file, name='upload_file'),
      path('process/<int:file_id>/',process_file, name='process_file'), 
]