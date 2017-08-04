from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Midia
from .forms import MidiaForm


# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

@login_required()
def midia(request, template_name='midias.html'):
    lista_midias = Midia.objects.all().order_by('-id')
    paginator = Paginator(lista_midias, 5) #Mostra 5 registros por página

    page = request.GET.get('page', 1)
    try:
        registers = paginator.page(page)
    except PageNotAnInteger:
        registers = paginator.page(1)
    except EmptyPage:
        registers = paginator.page(paginator.num_pages)

      # Get the index of the current page
    index = registers.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # My new page range
    page_range = paginator.page_range[start_index:end_index]
    
    return render(request, template_name, { 
        'registers': registers,
        'page_range': page_range,
        })


    

def salvar_form_midia(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            #import pdb; pdb.set_trace()
            data['form_is_valid'] = True
            midias = Midia.objects.all().order_by('-id')
            data['html_midia_list'] = render_to_string('listaMidias.html', {
                'midias': midias
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def midia_new(request):
    if request.method == 'POST':
        form = MidiaForm(request.POST)
    else:
        form = MidiaForm()
    return salvar_form_midia(request, form, 'cadastraMidia.html')


def midia_edit(request, pk):
    midia = get_object_or_404(Midia, pk=pk)
    if request.method == 'POST':
        form = MidiaForm(request.POST, instance=midia)
    else:
        form = MidiaForm(instance=midia)
    return salvar_form_midia(request, form, 'alteraMidia.html')

def midia_remove(request, pk):
    midia = get_object_or_404(Midia, pk=pk)
    data = dict()
    if request.method == 'POST':
        midia.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        midias = Midia.objects.all()
        data['html_midia_list'] = render_to_string('listaMidias.html', {
            'midias': midias
        })
    else:
        context = {'midia': midia}
        data['html_form'] = render_to_string('deletaMidia.html',
            context,
            request=request,
        )
    return JsonResponse(data)

