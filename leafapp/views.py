import json
from django.http.response import JsonResponse
from django.shortcuts import render
from leafapp.models import Maptype, Marker, Novel
from leafapp.serializer import MarkerSerializer
from .forms import MapForm, PointForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.
def home(request):
    books = Novel.objects.all()
    context = {
        'books' : books
    }
    return render(request,"first.html", context)


def index(request, pk):
    if request.method == "POST":
        # check if user is author of novel
        olamide = get_object_or_404(Novel, pk=pk, author__user=request.user)
        form = MapForm(request.POST)
        if form.is_valid():
            ola = form.save(commit=False)
            ola.novel = olamide
            ola.save()
            return HttpResponse('saved')
        return HttpResponse('invalid')
    # get map type for display
    types = Maptype.objects.filter(novel__id=pk)
    context = {
        'types': types
    }

    return render(request,'index.html', context)





def store_points(request, pk):
    # store new point for a novel map
    if request.is_ajax and request.method == "POST":
        

        # get the form data
        body = json.loads(request.body
        )

        # check if book is owned by user
        object = get_object_or_404(Novel, pk=body['novel'], author__user=request.user)
        
        form = PointForm(data=body)


        # save the data and after fetch the object in instance

        if form.is_valid():

            instance = form.save(commit=False)

            # just before saving add user

            instance.claimed_by = request.user

            instance.save()

            ser_instance = 'saved'

            # send to client side.

            return JsonResponse({"instance": ser_instance}, status=200)

        else:

            # some form errors occured.

            return JsonResponse({"error": form.errors}, status=400)


    # send get html, display the maptypes,for a pariculaar novel
    novel = Novel.objects.get(pk=pk)
    types = Maptype.objects.filter(novel = novel)
    context = {
        "novel" : pk,
        "types" : types
    }

    return render(request, 'third.html', context)



def display(request, novel, type):
    # get all markers belonging to a particular novel 
    points =  Marker.objects.filter(novel=novel, type=type)
    serializer = MarkerSerializer(points, many=True) 
    context = {
        'points': serializer.data
    }
    return render(request, "secound.html" , context)



    
