from django.shortcuts import render

# Create your views here.
def home(request):
    """A view that displays the home page"""
    return render(request, "home.html")

def deliveries(request):
    """A view that displays the deliveries page"""
    return render(request, "deliveries.html")

def track(request):
    """A view that displays the track page"""
    return render(request, "track.html")

def contact(request):
    """A view that displays the contact page"""
    return render(request, "contact.html")

def faq(request):
    """A view that displays the help page"""
    return render(request, "help.html")

def sizes(request):
    """A view that displays the sizes page"""
    return render(request, "sizes.html")

def metal(request):
    """A view that displays the metal page"""
    return render(request, "metal.html")