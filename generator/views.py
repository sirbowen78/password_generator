from django.shortcuts import render
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random


# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def password(request):
    # Initialize password to empty string
    generated_password = ""

    length = int(request.GET.get("length"))

    # Get the drop down value, if no value default to 12
    length = int(request.GET.get("length", 12))

    # Default lower case characters
    characters = list(ascii_lowercase)

    # Extend the list of uppercase letters if chosen
    if request.GET.get("uppercase"):
        characters.extend(list(ascii_uppercase))

    # Extend the list of digits if chosen
    if request.GET.get("numbers"):
        characters.extend(list(digits))

    # Extend the list of punctuation if chosen
    if request.GET.get("special"):
        characters.extend(list(punctuation))

    for _ in range(length):
        generated_password += random.choice(characters)

    return render(request, "generator/password.html", {"password": generated_password})
