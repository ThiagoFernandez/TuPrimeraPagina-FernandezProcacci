from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, ProfileForm
from .models import Profile


def signup(request):

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            Profile.objects.create(user=user)

            login(request, user)

            return redirect("inicio")

    else:

        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})


@login_required
def profile(request):

    profile = Profile.objects.get(user=request.user)

    return render(request, "accounts/profile.html", {"profile": profile})


@login_required
def edit_profile(request):

    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":

        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():

            form.save()

            return redirect("profile")

    else:

        form = ProfileForm(instance=profile)

    return render(request, "accounts/edit_profile.html", {"form": form})