from django.shortcuts import render, redirect
from django.views import View
from .models import Transfer, TransferItem
from goods.models import Goods
from .form import NewTransferForm, TransferItemsForm, ReportForm
from django.contrib import messages


class TransferView(View):
    def get(self, request):
        tr = Transfer.objects.all()
        if request.GET.get('from_date'):
            tr = tr.filter(date__gte=request.GET.get('from_date'))
        if request.GET.get('to_date'):
            tr = tr.filter(date__lte=request.GET.get('to_date'))   
        if request.GET.get('mode'):
            tr = tr.filter(mode=request.GET.get('mode'))   
        if request.GET.get('goods'):
            for i in tr:
                item_list = [j.goods.name for j in i.items.all()]
                if request.GET.get('goods') not in item_list:
                    tr = tr.exclude(id=i.id)   
        form = ReportForm
        return render(request, 'home/home.html', {'transfer':tr, 'form':form})


class NewTransferView(View):
    def get(self, request):
        form_trans = NewTransferForm
        goods = None
        if request.session.get('goods'):
            goods = request.session.get('goods')
        return render(request, 'home/new.html', {'form_trans':form_trans, 'goods':goods})

    def post(self, request):
        form_trans = NewTransferForm(request.POST)
        if form_trans.is_valid():
            cd_trans = form_trans.cleaned_data
            if cd_trans['mode'] == 'exit':
                for item in request.session.get('goods').values():
                    if not Goods.objects.get(name=item['name']).CheckInventory(int(item['quantity'])):
                        messages.warning(request, f'درخواست شما برای کالای {item["name"]} بیشتر از موجودی انبار می باشد.', 'warning')
                        return redirect('home:new')
            
            tr = form_trans.save()
            for item in request.session.get('goods').values():
                gd = Goods.objects.get(name=item['name'])
                TransferItem.objects.create(
                    transfer = tr,
                    goods = gd,
                    quantity = int(item['quantity']),
                )
                gd.UpdateInventory(tr.mode, int(item['quantity']))
            del request.session['goods']
            messages.success(request, 'حواله شما با موفقیت ثبت گردید.')
        return redirect('home:home')


class DetailTransferView(View):
    def get(self, request, id):
        tr = Transfer.objects.get(id=id)
        return render(request, 'home/detail.html', {'transfer':tr})


class AddGoodsToTransferView(View):
    def get(self, request):
        form = TransferItemsForm
        return render(request, 'home/add_goods.html', {'form':form})
    
    def post(self, request):
        form = TransferItemsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            gd_id = str(cd['goods'].id)
            if not request.session.get('goods'):
                request.session['goods'] = {}
            if not request.session['goods'].get(gd_id):
                request.session['goods'][gd_id] = {
                        'name' : cd['goods'].name,
                        'quantity' : cd['quantity'],
                }
            else:
                request.session['goods'][gd_id]['quantity'] += cd['quantity']
        request.session.modified = True
        return redirect('home:new')


class RemoveView(View):
    def get(self, request, id):
        request.session['goods'].pop(str(id))
        request.session.modified = True
        return redirect('home:new')

