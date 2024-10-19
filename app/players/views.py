from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from players.models import Participant
from .models import Image
import cloudinary.uploader


def players_views(request):
    players = Participant.objects.all()
    search = request.GET.get('search')
    if search:
        players = players.filter(name__icontains = search)
    return render(request,'players.html',
    {'players': players})

def index_views(request):
    return render(request, 'login.html')

def gallery_views(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)  # Inclui request.FILES
        if form.is_valid():
            # Use o campo do formulário diretamente
            uploaded_image = form.cleaned_data['image_file']  # Obtenha o arquivo enviado do formulário

            # Faça o upload para o Cloudinary
            upload_result = cloudinary.uploader.upload(uploaded_image)  # Envia o arquivo

            # Salve os dados no banco de dados
            new_image = Image(
                title=form.cleaned_data['title'],
                image=upload_result['url'],  # Salve a URL da imagem
                public_id=upload_result['public_id']  # Salve o public_id se necessário
            )
            new_image.save()
            return redirect('gallery_list')
    else:
        form = ImageForm()

    images = Image.objects.all()  # Obtenha todas as imagens para exibição
    return render(request, 'gallery.html', {'form': form, 'images': images})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)  # Obtém a imagem a ser excluída

    # Exclui a imagem do Cloudinary usando o public_id
    # O public_id deve ser salvo corretamente no modelo durante o upload
    cloudinary.uploader.destroy(image.public_id)  # Use o public_id da imagem

    # Exclui o registro da imagem no banco de dados
    image.delete()

    return redirect('gallery_list')  # Redireciona para a galeria após a exclusão