from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from App_build.models import CsvUpload, ClassifierInfo
from App_build.forms import CsvForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

import timeit
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import warnings
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import time

@login_required
def build1(request):
    form = CsvForm()
    if request.method == 'POST':
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('build2'))

    return render(request, 'App_build/build1.html', {'form': form})

def build2(request):
    csvs = CsvUpload.objects.all()
    return render(request, 'App_build/build2.html', context={'csvs': csvs})


def build3(request):
    if request.method == 'POST':
        csvfile = request.POST.get("csvfile")
        timestr = time.strftime("%Y%m%d-%H%M%S")

        warnings.filterwarnings('ignore')

        # import csv file data
        dataset=pd.read_csv('media/' + csvfile)

        X = dataset.iloc[:, :-1]  # Features (all columns except the last)
        y = dataset.iloc[:, -1]   # Target variable (last column)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        start = timeit.default_timer()
        clf=RandomForestClassifier(n_estimators=100)
        clf.fit(X_train,y_train)
        stop = timeit.default_timer()
        train_time= stop - start
        start = timeit.default_timer()
        y_pred=clf.predict(X_test)
        stop = timeit.default_timer()
        test_time= stop - start
        cr = precision_recall_fscore_support(y_test,y_pred, average='macro')
        accuracy = accuracy_score(y_test, y_pred)
        precision = cr[0]
        recall = cr[1]
        f1score = cr[2]

        pickle.dump(clf,open("media/" + "model" + timestr + ".sav", "wb"))
        pickle.dump(scaler, open("media/" + "scalermodel" + timestr + ".sav", "wb"))

        dataset = csvfile
        model = "model" + timestr + ".sav"
        scaled = "scalermodel" + timestr + ".sav"
        ClassifierInfo.objects.create(dataset=dataset, classifier_model=model, classifier_scaler=scaled, accuracy=accuracy, f1score=f1score, precision=precision, recall=recall)


        context = {
        'precision': precision,
        'recall': recall,
        'f1score': f1score,
        'accuracy': accuracy,
        'model': model,
        }
        return render(request, 'App_build/build3.html', context)