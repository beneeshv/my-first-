from django.shortcuts import render

def index(request):
    return render(request, 'home.html')  # Ensure this template exists

def about(request):
    return render(request, 'about.html')  # Another example

from django.shortcuts import render

# Example data for blog posts
from django.shortcuts import render

# Example data for blog posts
def home(request):
    posts = [
        {
            'title': 'The Future of Artificial Intelligence',
            'author': 'John Doe',
            'date': 'January 21, 2025',
            'excerpt': 'Exploring how AI will shape the future of humanity...',
            'image': 'ai_future.jpg',
            'link': '#',
        },
        {
            'title': 'How to Stay Productive While Working Remotely',
            'author': 'Jane Smith',
            'date': 'January 15, 2025',
            'excerpt': 'Practical tips to make remote work more efficient...',
            'image': 'remote_work.jpg',
            'link': '#',
        },
        {
            'title': 'Top 10 Programming Languages to Learn in 2025',
            'author': 'Tech Guru',
            'date': 'January 10, 2025',
            'excerpt': 'A guide to the most in-demand programming languages...',
            'image': 'programming.jpg',
            'link': '#',
        },
    ]
    return render(request, 'home.html', {'posts': posts})
