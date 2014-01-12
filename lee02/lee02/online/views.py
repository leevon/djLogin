from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class UserForm(forms.Form):
	userName = forms.CharField()

def login(req):
	if req.method == "POST":
		uf = UserForm(req.POST)
		if uf.is_valid():
			userName = uf.cleaned_data["userName"]
			print userName
			#return HttpResponse('login ok')
			req.session["userName"] = userName
			return HttpResponseRedirect("/lee02/index/")
	else:
		uf = UserForm()
	return render_to_response("login.html", {"uf":uf})



def index(req):
	userName = req.session.get("userName", "anybody")
	#return HttpResponse('hello ' + userName)
	return render_to_response("index.html", {"userName":userName})

def logout(req):
	del req.session["userName"]
	return HttpResponse("logout ok")