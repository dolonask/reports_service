from django.urls import path
from .views import create_card

urlpatterns = [
    # path('source/', create_source, name='CreateSource'),
    path('create/', create_card, name='CreateCard'),
    # path('add_files/<int:id>/', add_files, name='AddFiles')
]
