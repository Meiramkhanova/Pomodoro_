from django.shortcuts import render

def main_page(request):
    return render(request, 'main_page.html')

def error_400(request, exception):
    # your custom error handling logic for Bad Request (400) error
    return render(request, '400.html', status=400)

def error_403(request, exception):
    # your custom error handling logic for Forbidden (403) error
    return render(request, '403.html', status=403)

def error_404(request, exception):
    # your custom error handling logic for Not Found (404) error
    return render(request, '404.html', status=404)

def error_500(request):
    # your custom error handling logic for Internal Server Error (500) error
    return render(request, '500.html', status=500)