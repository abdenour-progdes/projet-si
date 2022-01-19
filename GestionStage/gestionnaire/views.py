from django.shortcuts import redirect, render
from .forms import EncadreurForm, PromoteurForm,OrganismeForm
from .models import Encadreur, Promoteur,Organisme



def index(request):
    return render(request,"dashboard/index.html")








def promoteur(request):
    items = Promoteur.objects.all()
    
    if request.method == 'POST':
        form = PromoteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-promoteur')
    else:
        form = PromoteurForm()
    context = {
        'items': items,
        'form' : form,
    }
    return render(request, 'dashboard/promoteur.html', context)


def promoteurDelete(request, pk):
    item = Promoteur.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-promoteur')
    context = {
        'item': item
    }
    return render(request, 'dashboard/promoteur_delete.html',context)


def promoteurEdit(request, pk):
    item = Promoteur.objects.get(id=pk)
    if request.method == 'POST':
        form = PromoteurForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-promoteur')
    else:
        form = PromoteurForm(instance=item)
    
    context = {
        'form': form,
    }
    return render(request, 'dashboard/promoteur_edit.html', context)









def encadreur(request):
    items = Encadreur.objects.all()
    if request.method == 'POST':
        form = EncadreurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-encadreur')
    else:
        form = EncadreurForm()
    context = {
        'items': items,
        'form' : form,
    }
    return render(request, 'dashboard/encadreur.html', context)


def encadreurDelete(request, pk):
    item = Encadreur.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-encadreur')  
    context = {
        'item': item
    }    
    return render(request, 'dashboard/encadreur_delete.html', context)


def encadreurEdit(request, pk):
    item = Encadreur.objects.get(id=pk)
    if request.method == 'POST':
        form = EncadreurForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-encadreur')
    else:
        form = EncadreurForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/encadreur_edit.html', context)






def organisme(request):
    items = Organisme.objects.all()
    if request.method == 'POST':
        form = OrganismeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Organisme')
    else:
        form = OrganismeForm()
    context = {
        'items': items,
        'form' : form,
    }
    return render(request, 'dashboard/Organisme.html', context)


def OrganismeDelete(request, pk):
    item = Organisme.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Organisme')
    context = {
        'item': item
    }
    return render(request, 'dashboard/Organisme_delete.html',context)


def OrganismeEdit(request, pk):
    item = Organisme.objects.get(id=pk)
    if request.method == 'POST':
        form = OrganismeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Organisme')
    else:
        form = OrganismeForm(instance=item)
    
    context = {
        'form': form,
    }
    return render(request, 'dashboard/Organisme_edit.html', context)