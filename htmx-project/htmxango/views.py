from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User

def user_card(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.description = request.POST.get("description")
        user = get_object_or_404(User, id=user_id)
        user.save()
        return render(request, "user_card.html", {"user": user})  # Reload card after saving

    return render(request, "user_card.html", {"user": user, "editing": request.GET.get("edit") is not None})

def home(request):
    return redirect('/user/1/')  # Redirect to a valid user (change ID as needed)
