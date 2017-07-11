from django.shortcuts import render
from .models import Midia
from .forms import MidiaForm

from django.shortcuts import render, redirect

def midia(request, template_name='midia_list.html'):
    data = {}
    data['lista_midias'] = Midia.objects.all()
    return render(request, template_name, data)

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
