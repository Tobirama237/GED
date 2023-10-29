from django.urls import path
from . import views

urlpatterns = [
    #path to home page
    #path('', views.index, name="index"),
    #path to list documents
    path('documents/', views.documents, name="documents"),
    #path to have document detail
    path('document/<str:pk>/', views.document, name="document"),
    #path to create a new document
    path('create-document/', views.createDocument, name="create-document"),
    #path to update a document
    path('update-document/<str:pk>/', views.updateDocument, name="update-document"),
    #path to delete a document
    path('delete-document/<str:pk>/', views.deleteDocument, name="delete-document"),
]