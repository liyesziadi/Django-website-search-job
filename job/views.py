from django.shortcuts import redirect, render
from .models import Job,Category,Apply,image_upload
from django.core.paginator import Paginator
from .forms import ApplayForm,JobForm
from django.urls import reverse

# Create your views here.

def sum_number(v1,v2):
    return v1+v2

def GetNumbersFromGET(req):
    page_number=req.GET.get('page')
    if not page_number :
        page_number=1 
    return float(page_number)*100


def job_list(request):
    job_list = Job.objects.all()

    paginator=Paginator(job_list,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if not page_number :
        page_number=1   
    val2=sum_number(int(page_number),100) 
    get_nbr_p=GetNumbersFromGET(request)

    context = {
        'job_list':page_obj,
        'val2':val2,
        'get_nbr_p':get_nbr_p,
        
    }
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
  
    if request.method=='POST':
        form=ApplayForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_detail
            myform.save()
    else:
       form=ApplayForm()
        

    context = {
        'job_detail': job_detail,
        'form1':form,
    }
    return render(request, 'job/job_detail.html', context)

def add_job(request):
        if request.method=='POST':
            form=JobForm(request.POST,request.FILES)
            if form.is_valid:
                myform= form.save(commit=False)
                myform.owner=request.user
               # myform.image=Job.image
                myform.save()
                return redirect(reverse('job_list'))
        else:
            form=JobForm()


        context={

            'form':form,
        }

        return render(request,'job/add_job.html',context)
