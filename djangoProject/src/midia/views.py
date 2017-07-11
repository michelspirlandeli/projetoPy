from django.shortcuts import render
from .models import Midia
#from django.contrib import messages
from django.forms import ModelForm

from .forms import MidiaForm
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def midia_list(request):
    queryset_list = Midia.objects.all()
    paginator = Paginator(queryset_list, 5)
    page_request_var = "página"
    page = request.GET.get(page_request_var)
    context = {
        "title": "Lista",
        "page_request_var": page_request_var,
        "object_list": queryset,
    }
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)    
    return render(request, "midia_list.html", context)


def midia_new(request):
    form = MidiaForm(request.POST or None)
    context = {
            "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        print (form.cleaned_data.get("analista"))
        instance.save()
        # message success
        #messages.success(request, "Criado com sucesso!")
        return HttpResponseRedirect(instance.get_absolute_url())
        
    return render(request, "midia_form.html", context)




def midia_edit(request, slug=None):
    instance = get_object_or_404(Midia, slug=slug)
    form = MidiaForm(request.POST or None, instance=instance)
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request)
        return HttpResponseRedirect(instance.get_absolute_url())
    
    return render(request, "midia_form.html", context)

def midia_remove(request, slug=None):
    instance = get_object_or_404(Midia, slug=slug)
    if request.method == "POST":
        midia.delete()
        return redirect('list')
    return render(request, 'midia_delete.html', {'midia': midia})