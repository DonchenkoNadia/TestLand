from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render 
import logging
import sys, os

# Get an instance of a logger
logger = logging.getLogger("dev_info")

def home(request):
	return(request, "home.html")

def index(request):
	#print "Bugaga"
	# Log an error message
    logger.debug('A debug message for sure ')
    #logger.debug('sys.argv[0] =', sys.argv[0])
    #logger.debug('path =', os.path.dirname(sys.argv[0]))
    #logger.debug('full path =', os.path.abspath(pathname))
    return HttpResponse("Hello, world. You're at the polls indexing")

'''def index(request):
	template = loader.get_template('testland/index.html')
	print("Path at terminal when executing this file")
	print(os.getcwd() + "\n")
	print("Bingo!")
	context = RequestContext(request, { a_text: "Some optimistic text!",})
	return HttpResponse(template.render(context)) '''

#from django.contrib.auth.models import User

#def index(request):
#    usr_list = User.objects.all()[:5]
#    context = {'usr_list': usr_list}
#    return render(request, '/index.html', context)