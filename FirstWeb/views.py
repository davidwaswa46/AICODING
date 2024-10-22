from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

def about_page(request):
    # You can add any additional context data here if needed
    context = {
        'page_title': 'About Us',
        # Add more context data if needed
    }
    return render(request, 'About.html', context)

