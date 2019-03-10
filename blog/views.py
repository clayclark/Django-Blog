from django.shortcuts import render

posts = [
    {
        'author': 'Clay',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 23, 2019'
    },
    {
        'author': 'Chlo',
        'title': 'Blog Post 2',
        'content': '2 post content',
        'date_posted': 'January 1, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

