from django.shortcuts import render, redirect
from django.http import HttpResponse


def inicio(request):
    return render(request, "base/base.html", {})
