from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.request import Request
from rest_framework.response import Response


@login_required
def dashboard(request: Request) -> Response:
    return render(request, "dashboard/dashboard.html")
