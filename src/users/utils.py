from .models import Profile
from django.db.models import Q



def searchProfiles(request):
    search_query = ''

    if request.GET.get('mot_cle'):
        search_query = request.GET.get('mot_cle')

    profiles = Profile.objects.filter(
        Q(name__icontains=search_query) | 
        Q(fonction__icontains=search_query)
    )
    
    return profiles, search_query

#def searchDocuments(request):
