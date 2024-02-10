from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Product

class Homeview(View):
    def get(self,request):
        return render(request,template_name='home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,template_name="productinput.html")

class Insertview(View):
    def get(self,request):
        p_id=int(request.GET['t1'])
        p_name=request.GET['t2']
        p_cost=float(request.GET['t3'])
        p_mfdt=request.GET['t4']
        p_expdt=request.GET['t5']
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        res = HttpResponse("Product inserted successfully")
        return res

class Dispalyview(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dict={ "records": qs}
        return render(request,template_name='display.html',context=con_dict)

class DeleteInputView(View):
    def get(self,request):
        return render(request,template_name='delete.html')


class DeleteView(View):
    def get(self,request):
        p_id=int(request.GET['t1'])
        prod=Product.objects.filter(pid=p_id)
        prod.delete()
        resp=HttpResponse("Product deleted")
        return resp

class UpdateInputView(View):
    def get(self,request):
        return render(request,template_name="updateinput.html")

class UpdateView(View):
    def post(self,request):
        p_id=int(request.POST['t1'])
        p_name=request.POST['t2']
        p_cost=float(request.POST['t3'])
        p_mfdt=request.POST['t4']
        p_expdt=request.POST['t5']
        prop=Product.objects.get(pid=p_id)
        prop.pname=p_name
        prop.pcost=p_cost
        prop.pmfdt=p_mfdt
        prop.pexpdt=p_expdt
        prop.save()
        resp = HttpResponse("product updated successfully")
        return resp


