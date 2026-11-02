from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import LugarForm
from .models import Categoria, LugarPatrimonial


# ---------- Zona pública ----------
def inicio(request):
    destacados = LugarPatrimonial.objects.select_related('categoria').order_by('-id')[:3]
    return render(request, 'catalogo/inicio.html', {'destacados': destacados})


def catalogo(request):
    return render(request, 'catalogo/catalogo.html', {
        'lugares': LugarPatrimonial.objects.select_related('categoria'),
        'categorias': Categoria.objects.all(),
    })


def detalle_lugar(request, pk):
    lugar = get_object_or_404(LugarPatrimonial.objects.select_related('categoria'), pk=pk)
    return render(request, 'catalogo/detalle.html', {'lugar': lugar})


def lugares_por_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'catalogo/catalogo.html', {
        'lugares': categoria.lugares.select_related('categoria'),
        'categorias': Categoria.objects.all(),
        'categoria_actual': categoria,
    })


# ---------- Zona privada ----------
@login_required
def gestion(request):
    lugares = LugarPatrimonial.objects.select_related('categoria')
    return render(request, 'catalogo/gestion.html', {'lugares': lugares})


@login_required
@permission_required('catalogo.add_lugarpatrimonial', raise_exception=True)
def lugar_crear(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            lugar = form.save()
            messages.success(request, 'Lugar agregado correctamente.')
            return redirect('detalle_lugar', pk=lugar.pk)
    else:
        form = LugarForm()
    return render(request, 'catalogo/lugar_form.html', {'form': form, 'titulo': 'Agregar lugar'})


@login_required
@permission_required('catalogo.change_lugarpatrimonial', raise_exception=True)
def lugar_editar(request, pk):
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)
    if request.method == 'POST':
        form = LugarForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lugar actualizado correctamente.')
            return redirect('detalle_lugar', pk=lugar.pk)
    else:
        form = LugarForm(instance=lugar)
    return render(request, 'catalogo/lugar_form.html', {'form': form, 'titulo': f'Editar: {lugar.nombre}'})