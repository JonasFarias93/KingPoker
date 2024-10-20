from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image
import cloudinary.uploader



def gallery_views(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.cleaned_data['image_file']  

            upload_result = cloudinary.uploader.upload(uploaded_image)

        
            new_image = Image(
                title=form.cleaned_data['title'],
                image=upload_result['url'],
                public_id=upload_result['public_id'] 
            )
            new_image.save()
            return redirect('gallery_list')
    else:
        form = ImageForm()

    images = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'form': form, 'images': images})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id) 


    cloudinary.uploader.destroy(image.public_id)

    image.delete()
    return redirect('gallery_list')