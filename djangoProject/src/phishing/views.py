from django.shortcuts import render
from .models import Phishing
from .forms import PhishingForm

from django.shortcuts import render, redirect

# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def phishing(request, template_name='phishing_list.html'):
    lista_phishings = Phishing.objects.all()
    paginator = Paginator(lista_phishings, 5) #Mostra 5 registros por página

    page = request.GET.get('page', 1)
    try:
        registers = paginator.page(page)
    except PageNotAnInteger:
        registers = paginator.page(1)
    except EmptyPage:
        registers = paginator.page(paginator.num_pages)


    return render(request, template_name, { 'registers': registers })

def phishing_new(request, template_name='phishing_create.html'):
    form = PhishingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_phishing')
    return render(request, template_name, {'form':form})

def phishing_edit(request, pk, template_name='phishing_update.html'):
    phishing = Phishing.objects.get(id=pk)

    form = PhishingForm(request.POST or None, instance=phishing)
    if form.is_valid():
        form.save()
        return redirect('list_phishing')
    return render(request, template_name, {'object': phishing, 'form': form})


def phishing_remove(request, pk, template_name='phishing_delete.html'):
    phishing = Phishing.objects.get(pk=pk)

    if request.method== 'POST':
        phishing.delete()
        return redirect('list_phishing')
    return render(request, template_name, {'object': phishing})
