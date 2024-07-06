from django.shortcuts import render,redirect
from health_app.models import Blog

# Create your views here.
def get_home_page(request):
    return render(request,'home.html',context={})

def get_yoga_page(request):
    return render(request,'yoga.html',context={})

def get_mental_health_page(request):
    return render(request,'mental_health.html',context={})

def blog_page(request):
    return render(request,'blog.html',context={} )

def save_data(request):
    name = request.POST['name']
    title = request.POST['title']
    content = request.POST['message']

    blog_data = Blog(name= name ,blog_name = title ,content = content )
    blog_data.save()
    return redirect('blog_page')

def get_all_blog(request):
    blog_data = Blog.objects.all()
    context = {
        'blog':blog_data
    }
    return render(request,'blog_display.html',context = context)
