from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post

def inicio(request):
    return render(request, "blog/inicio.html")


def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request, "blog/form.html", {
        "form": form,
        "titulo": "Crear Autor"
    })


def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request, "blog/form.html", {
        "form": form,
        "titulo": "Crear Categoría"
    })


def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request, "blog/form.html", {
        "form": form,
        "titulo": "Crear Post"
    })


def buscar_post(request):
    resultados = []
    if request.GET.get("titulo"):
        resultados = Post.objects.filter(
            titulo__icontains=request.GET["titulo"]
        )

    return render(request, "blog/buscar.html", {
        "resultados": resultados
    })
