from  django.http import HttpResponse



def hello_world(request):
	return HttpResponse("nidhal messelmani django heroku demo")