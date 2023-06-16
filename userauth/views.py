from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.views.generic import CreateView, FormView, RedirectView


from . forms import *
from . models import *

# Create your views here.


class SingUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'userauth/signup.html'
    success_url= '/'


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(self.request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        signform = self.form_class(data=request.POST)
        if signform.is_valid():
            user = signform.save(commit=False)
            password = signform.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            return redirect("userauth:login")
        else:
            return render(request, "userauth/signup.html", {"signform": signform})


class LoginView(FormView):
    success_url = "/"
    form_class = SignInForm
    template_name = "userauth/login.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if "next" in self.request.GET and self.request.GET["next"] != "":
            return self.request.GET["next"]
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, signform):
        auth.login(self.request, signform.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, signform):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(signform=signform))


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """

    url = "/login"

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return super(LogoutView, self).get(request, *args, **kwargs)

