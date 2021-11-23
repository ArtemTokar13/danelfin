from django.contrib import admin
from django.urls import path

from numbers_task.views import NumbersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NumbersView.as_view(), name='view'),
]
