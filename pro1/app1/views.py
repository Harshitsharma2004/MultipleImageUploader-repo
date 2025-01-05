from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import ImageUpload

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'app1/success.html')
    else:
        form = ImageForm()
    return render(request, 'app1/upload.html', {'form': form})

def view_images(request):
    images = ImageUpload.objects.all()
    return render(request, 'app1/view.html', {'images': images})
