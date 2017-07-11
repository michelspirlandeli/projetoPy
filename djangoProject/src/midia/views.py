from django.shortcuts import render
from .models import Midia
from .forms import MidiaForm

from django.shortcuts import render, redirect

# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def midia(request, template_name='midia_list.html'):
    lista_midias = Midia.objects.all()
    paginator = Paginator(lista_midias, 5) #Mostra 5 registros por página

    page = request.GET.get('page', 1)
    try:
        registers = paginator.page(page)
    except PageNotAnInteger:
        registers = paginator.page(1)
    except EmptyPage:
        registers = paginator.page(paginator.num_pages)


    return render(request, template_name, { 'registers': registers })

def midia_new(request, template_name='midia_create.html'):
    form = MidiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, template_name, {'form':form})

def midia_edit(request, pk, template_name='midia_update.html'):
    midia = Midia.objects.get(id=pk)

    form = MidiaForm(request.POST or None, instance=midia)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, template_name, {'object': midia, 'form': form})


def midia_remove(request, pk, template_name='midia_delete.html'):
    midia = Midia.objects.get(pk=pk)

    if request.method== 'POST':
        midia.delete()
        return redirect('list')
    return render(request, template_name, {'object': midia})
