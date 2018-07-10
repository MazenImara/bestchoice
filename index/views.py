from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.utils.translation import LANGUAGE_SESSION_KEY
from apps.forms import AppForm
from apps.models import Apk
import json


# Create your views here.
def switch_lang(request):

	url = request.GET.get('url')
	lang = request.GET.get('lang')
	if lang:
		activate(lang)
		request.session[LANGUAGE_SESSION_KEY] = lang
	if not url:
		url = '/'
	return HttpResponseRedirect(url)

def index(request):
	host = request.META['HTTP_HOST']
	if 'uropenn' in host:
		return iframe(request, 'https://www.uropenn.se/')
	else:
		return iframe(request, 'https://www.hm.com/bh/')

		

def manageApk(request):
	if request.method == 'POST':
		appForm = AppForm(request.POST, request.FILES)
		if appForm.is_valid():
			appForm.save()

	fun = request.GET.get('fun')
	id = request.GET.get('id')
	if fun:
		if fun == 'del' and id:
			try:
				apk = Apk.objects.get(id=id)
				apk.delete()
			except Exception as e:
				pass	


	files = Apk.objects.all()
	context = {
		'appForm': AppForm(),
		'files': files,
	}
	return render(request, 'manageApk.html', context)	

def iframe(request, fakeUrl):
	context = {
		'fakeUrl': fakeUrl,
	}
	return render(request, 'iframe.html', context)	