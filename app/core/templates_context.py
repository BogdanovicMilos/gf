import os


def export_vars(request):
    return {"BLOG_HOST": os.environ.get("BLOG_HOST", "")}
