from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

from .models import User,customer_detail,payment

from django.http import HttpResponse
def home_view(request):
    return render(request, 'home.html')

def personalloan_view(request):
    return render(request, 'personal loan.html')

def goldloan_view(request):
    return render(request, 'gold loan.html')

def homeloan_view(request):
    return render(request, 'home loan.html')

def educationloan_view(request):
    return render(request, 'education loan.html')

def vehicleloan_view(request):
    return render(request, 'vehicle loan.html')


def endpage_view(request):
    return render(request, 'end page.html')

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
               
                return redirect('home')
            else:
               
                return render(request, 'login.html', {'error': 'Invalid email or password.'})
        except User.DoesNotExist:
           
            return render(request, 'login.html', {'error': 'Invalid email or password.'})
    return render(request, 'login.html')

def create(request):
    print("method is",request.method)
    if request.method=='GET':
        return render(request,'details.html')
    else:
        f=request.POST['Firstname']
        l=request.POST['lastname']
        a=request.POST['age']
        ad=request.POST['address']
        cs=request.POST['creditscore']
        o=request.POST['occupation']
        e=request.POST['email']
        i=request.POST['income']
        lo=request.POST['loantype']
        print(f,l,a,ad,cs,o,e,i,lo)
        b=customer_detail.objects.create(first_name=f,last_name=l,age=a,address=ad,credit_score=cs,occupation=o,email=e,income=i,loan_type=lo)
        b.save()
        return redirect('/payments')
def payment_details(request):
    print("method is",request.method)
    if request.method=='GET':
        return render(request,'payments.html')
    else:
        holder=request.POST['holdername']
        acc=request.POST['accountnumber']
        bank=request.POST['bankname']
        ifsc=request.POST['IFSCnumber']
        b=payment.objects.create(holder_name=holder,acc_number=acc,bank_name=bank,ifsc_number=ifsc)
        b.save()
        return redirect('/endpage')
