from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import DocumentForm
from .models import Document

# function to render the home page
def index (request):
    return render(request,"docupload/index.html")

# function to render documents
def documents (request):
    search_query = ''

    if request.GET.get('mot_cle'):
        search_query = request.GET.get('mot_cle')

    documents = Document.objects.filter(
        Q(libelleDoc__icontains=search_query) | 
        Q(description__icontains=search_query) |
        Q(operator__name__icontains=search_query)
    )
    context = {'documents':documents, 'search_query': search_query}
    return render(request,"docupload/document.html", context)

#function to render a single document
def document (request, pk):
    document = Document.objects.get(id=pk)
    context = {'document': document}
    return render(request, "docupload/single-document.html", context)

# function to create a document
@login_required(login_url = "login")
def createDocument(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents')
    else:
        form = DocumentForm()
        context = {'form':form}
    return render(request, "docupload/document_form.html", context)

# function to update a document
@login_required(login_url = "login")
def updateDocument(request, pk):
    document = Document.objects.get(id=pk)
    form = DocumentForm(instance=document)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('documents')
    context = {'form':form}
    return render(request, "docupload/document_form.html", context)

#functioin to delete a document
@login_required(login_url = "login")
def deleteDocument(request, pk):
    document = Document.objects.get(id=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('documents')
    context = {'object': document}
    return render(request, "docupload/supprime_document.html", context)