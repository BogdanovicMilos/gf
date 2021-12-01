from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response


def index(request: Request) -> Response:
    return render(request, "marketing/index.html")


def media_buying(request: Request) -> Response:
    return render(request, "marketing/media_buying.html")


def facebook_ads(request: Request) -> Response:
    return render(request, "marketing/facebook_ads.html")


def google_ads(request: Request) -> Response:
    return render(request, "marketing/google_ads.html")


def enterprise_seo(request: Request) -> Response:
    return render(request, "marketing/enterprise_seo.html")


def local_seo(request: Request) -> Response:
    return render(request, "marketing/local_seo.html")


def search_engine_optimization(request: Request) -> Response:
    return render(request, "marketing/seo.html")


def about_us(request: Request) -> Response:
    return render(request, "marketing/about.html")


def get_in_touch(request: Request) -> Response:
    return render(request, "marketing/contacts.html")


def saas_marketing(request: Request) -> Response:
    return render(request, "marketing/saas_marketing.html")
