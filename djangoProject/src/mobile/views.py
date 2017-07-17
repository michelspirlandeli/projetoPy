from django.shortcuts import render
from .models import Mobile
from .forms import MobileForm

from django.shortcuts import render, redirect

# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def mobile(request, template_name='mobile_list.html'):
    lista_mobiles = Mobile.objects.all()
    paginator = Paginator(lista_mobiles, 5) #Mostra 5 registros por página

    page = request.GET.get('page', 1)
    try:
        registers = paginator.page(page)
    except PageNotAnInteger:
        registers = paginator.page(1)
    except EmptyPage:
        registers = paginator.page(paginator.num_pages)


    return render(request, template_name, { 'registers': registers })

def mobile_new(request, template_name='mobile_create.html'):
    form = MobileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_mobile')
    return render(request, template_name, {'form':form})

def mobile_edit(request, pk, template_name='mobile_update.html'):
    mobile = Mobile.objects.get(id=pk)

    form = MobileForm(request.POST or None, instance=mobile)
    if form.is_valid():
        form.save()
        return redirect('list_mobile')
    return render(request, template_name, {'object': mobile, 'form': form})


def mobile_remove(request, pk, template_name='mobile_delete.html'):
    mobile = Mobile.objects.get(pk=pk)

    if request.method== 'POST':
        mobile.delete()
        return redirect('list_mobile')
    return render(request, template_name, {'object': mobile})
