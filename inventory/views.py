from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
# from .forms import ItemForm


# Create your views here.

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity']


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_item')

    else:
        form = ItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})

@login_required
def home(request):
    query = request.GET.get('q')
    if query:
        items_list = Item.objects.filter(
                Q(name__icontains=query)
        )
    else:
        items_list = Item.objects.all()

    paginator = Paginator(items_list, 5) # show 5 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'inventory/item_list.html', {'page_obj': page_obj})
 
@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/edit_item.html', {'form': form, 'item': item})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Auto-login after register
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'inventory/register.html', {'form': form})
























