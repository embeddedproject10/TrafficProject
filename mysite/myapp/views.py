from django.shortcuts import render

# Create your views here.
def is_Crowded(request,place_name_input,crowded_input):
	p=Places.objects.get(place_name=place_name_input)
	p.is_Crowded = crowded_input
	p.save()
	return p.crowded