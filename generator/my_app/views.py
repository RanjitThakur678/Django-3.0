from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):

    return render(request,'generator/home.html')

def password(request):
    chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/*^%$#@!')
    
    new_pass = ''.join(random.sample(chars,8))
    # new_pass = ''
    # for s in range(length):
    #     new_pass += random.choice(chars)


    return render(request,'generator/password.html',{'password':new_pass})
