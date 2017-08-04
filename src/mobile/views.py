from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Mobile
from .forms import MobileForm

# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required


def mobile(request, template_name='mobiles.html'):
    lista_mobiles = Mobile.objects.all().order_by('-id')
    paginator = Paginator(lista_mobiles, 5) #Mostra 5 registros por página

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


def salvar_form_mobile(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            #import pdb; pdb.set_trace()
            data['form_is_valid'] = True
            mobiles = Mobile.objects.all().order_by('-id')
            data['html_mobile_list'] = render_to_string('listaMobiles.html', {
                'mobiles': mobiles
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def mobile_new(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
    else:
        form = MobileForm()
    return salvar_form_mobile(request, form, 'cadastraMobile.html')


def mobile_edit(request, pk):
    mobile = get_object_or_404(Mobile, pk=pk)
    if request.method == 'POST':
        form = MobileForm(request.POST, instance=mobile)
    else:
        form = MobileForm(instance=mobile)
    return salvar_form_mobile(request, form, 'alteraMobile.html')

def mobile_remove(request, pk):
    mobile = get_object_or_404(Mobile, pk=pk)
    data = dict()
    if request.method == 'POST':
        mobile.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        mobiles = Mobile.objects.all()
        data['html_mobile_list'] = render_to_string('listaMobiles.html', {
            'mobiles': mobiles
        })
    else:
        context = {'mobile': mobile}
        data['html_form'] = render_to_string('deletaMobile.html',
            context,
            request=request,
        )
    return JsonResponse(data)