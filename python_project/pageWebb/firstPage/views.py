from django.shortcuts import render, redirect
from django.http import HttpResponse
from sklearn.preprocessing import StandardScaler
from joblib import load
import pickle
import pandas as pd
import numpy as np


model = pickle.load(open('./models/model.pkl', 'rb'))
# Create your views here.

def index(request):
    print (request)
    return render(request,'index.html')

def predictPrice(request):
    print (request)
    print (request)
    print (request)
    prix=0
    if request.method =='POST':
        temp={}
        temp['surface'] = int(request.POST.get('surface'))
        temp['nb_Pieces'] = int(request.POST.get('nb_p'))
        temp['nb_chambre'] = int(request.POST.get('nb_c',0.0))
        temp['nb_Salles_de_bains'] = int(request.POST.get('nb_s',0.0))
        temp['etage'] = int(request.POST.get('etage',0.0))
        temp['ville'] = int(request.POST.get('ville',0.0)) 
        testDtaa=pd.DataFrame(temp,index=[0]) 
        prix=model.predict(testDtaa)[0]
        prix=int(prix)
        print("prix =  ",prix)
        request.session['prix']=prix
        return redirect('test')
    context={'prix':prix}
    return render(request,'predictPrice.html')

def test(request):
    prix=request.session['prix']
    prix=int(prix)
    print(prix)
    context={'prix':prix}
    return render(request,'test.html',context)
