from django.shortcuts import render
import os
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from sklearn.linear_model import LinearRegression

from rest_framework.parsers import JSONParser
from rest_framework import status
from datetime import datetime
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression,Ridge,Lasso,RidgeCV, ElasticNet, LogisticRegression

from .models import AutismRecord , User , FeedBack , AutismRecordAdult ,Clinic
from .serializers import AutismRecordSerializer ,UserCreateSerializer
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


class AutismRecordView(viewsets.ModelViewSet):
    queryset = AutismRecord.objects.all()
    serializer_class = AutismRecordSerializer



@api_view(['Post'])
def signup(request):
    date=datetime.now().strftime("%d/%m/%y %H:%M")
    return Response(status=status.HTTP_200_OK)


@api_view(['Post'])
@permission_classes([AllowAny])
def childrenAutismSpectrumTest(request):
    data = pd.json_normalize(data_prepr(request.data))
    print(data)
    user = request.user

    if user.is_anonymous : user= User.objects.get(email='admin@admin.com')
    try:
        print(os.path)
        model = joblib.load(open("API_app/model/randomForest.sav","rb"))
        data = data_pre_proccess(data)
        print(data)
        y_prediction = model.predict(data)[0]
        percentage = model.predict_proba(data)[0][1]
        data_to_save =request.data
        data_to_save['percentage']=percentage
        data_to_save['y_prediction']=y_prediction
        data_to_save['user']=user
        AutismRecord.save_record(data_to_save)
        clinic = Clinic.objects.get(email="Jorsca.jo@gmail.com")
        res = {"result": "{}".format(y_prediction), 'percentage': "{}".format(percentage), "clinic_name": clinic.name
              ,"clinic_phone_number": clinic.phone_number, "clinic_email": clinic.email,
               "clinic_location": clinic.location}
        return HttpResponse (json.dumps(res), content_type="application/json" , status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(e.args , status.HTTP_400_BAD_REQUEST)

@api_view(['Post'])
@permission_classes([AllowAny])
def AdultAutismSpectrumTest(request):
    data = data_prepr_adult(request.data)
    my_data = pd.json_normalize(data)
    user = request.user
    if user.is_anonymous : user= User.objects.get(email='admin@admin.com')
    try:
        print(os.path)
        model = joblib.load(open("API_app/model/randomForestAdult.sav","rb"))
        data = data_pre_proccess_adult(my_data)
        y_prediction = model.predict(data)[0]
        percentage = model.predict_proba(data)[0][1]
        data_to_save =request.data
        data_to_save['percentage']=percentage
        data_to_save['y_prediction']=y_prediction
        data_to_save['user']=user
        AutismRecordAdult.save_record(data_to_save)
        clinic = Clinic.objects.get(email="Jorsca.jo@gmail.com")
        res={"result":"{}".format(y_prediction),'percentage':"{}".format(percentage) , "clinic_name":clinic.name
             ,"clinic_phone_number":clinic.phone_number , "clinic_email":clinic.email,"clinic_location":clinic.location}
        return HttpResponse (json.dumps(res), content_type="application/json" , status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(e.args , status.HTTP_400_BAD_REQUEST)


def data_pre_proccess(data):
    data.drop(['Who_completed_the_test'], axis=1, inplace=True)
    data.drop(['Why_are_you_taken_the_screening'], axis=1, inplace=True)
    data.drop(['class_variable'], inplace=True, axis=1)
    data.drop(['percentage'], inplace=True, axis=1)
    data.drop(['user'], inplace=True, axis=1)
    data.Jaundice= data.Jaundice.map(dict(yes=1, no=0))
    data.rename(columns={"Age_mons": "Age_Mons", "gender": "Sex"},inplace=True)
    return data

def data_pre_proccess_adult(data):
    data.drop(['Who_completed_the_test'], axis=1, inplace=True)
    data.drop(['Why_are_you_taken_the_screening'], axis=1, inplace=True)
    data.drop(['class_variable'], inplace=True, axis=1)
    data.drop(['percentage'], inplace=True, axis=1)
    data.drop(['user'], inplace=True, axis=1)
    data.Jaundice = data.Jaundice.map(dict(yes=1, no=0))
    return data

def data_prepr(data):
    values1 = ['1','2']
    values2 = ['3','4','5']
    if data['A1'] in values1 :
        data['A1']=0
    elif data['A1'] in values2 :
        data['A1'] = 1
    if data['A2'] in values1 :
        data['A2']= 0
    elif data['A2'] in values2 :
        data['A2'] =1
    if data['A3'] in values1 :
        data['A3']= 0
    elif data['A3'] in values2 :
        data['A3'] = 1
    if data['A4'] in values1 :
        data['A4']=0
    elif data['A4'] in values2 :
        data['A4'] = 1
    if data['A5'] in values1 :
        data['A5']=0
    elif data['A5'] in values2 :
        data['A5'] = 1
    if data['A6'] in values1 :
        data['A6']=0
    elif data['A6'] in values2 :
        data['A6'] = 1
    if data['A7'] in values1 :
        data['A7']=0
    elif data['A7'] in values2 :
        data['A7'] = 1
    if data['A8'] in values1 :
        data['A8']=0
    elif data['A8'] in values2 :
        data['A8'] =1
    if data['A9'] in values1:
        data['A9']=0
    elif data['A9'] in values2:
        data['A9'] =1
    if data['A10'] in values1 :
        data['A10']=1
    elif data['A10'] in values2 :
        data['A10'] =0
    return data

def data_prepr_adult(data):
    values1 = ['1','2']
    values2 = ['3','4']
    if data['A1'] in values1 :
        data['A1']=1
    elif data['A1'] in values2 :
        data['A1'] = 0
    if data['A2'] in values1 :
        data['A2']= 0
    elif data['A2'] in values2 :
        data['A2'] =1
    if data['A3'] in values1 :
        data['A3']= 0
    elif data['A3'] in values2 :
        data['A3'] = 1
    if data['A4'] in values1 :
        data['A4']=0
    elif data['A4'] in values2 :
        data['A4'] = 1
    if data['A5'] in values1 :
        data['A5']=0
    elif data['A5'] in values2 :
        data['A5'] = 1
    if data['A6'] in values1 :
        data['A6']=0
    elif data['A6'] in values2 :
        data['A6'] = 1
    if data['A7'] in values1 :
        data['A7']=1
    elif data['A7'] in values2 :
        data['A7'] = 0
    if data['A8'] in values1 :
        data['A8']=1
    elif data['A8'] in values2 :
        data['A8'] =0
    if data['A9'] in values1:
        data['A9']=0
    elif data['A9'] in values2:
        data['A9'] =1
    if data['A10'] in values1 :
        data['A10']=1
    elif data['A10'] in values2 :
        data['A10'] =0
    return data

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserTestRecords(request):
    user =User.get_user_from_token(token=request.auth)
    records = AutismRecord.objects.filter(user=user)
    return HttpResponse(serializers.serialize('json',records),content_type="application/json",status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def testAuth(request):
    return HttpResponse(request.auth , status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def hhh(request):
    if request.FILES:
        file=request.FILES['csv_file']
        return JsonResponse(data={"data":"ssssssssss"})
    else:
        return JsonResponse(data={"data":"ssssssssss"})


@api_view(['POST'])
@permission_classes([AllowAny])
def sendFeedBack(request):
    if request.user.is_anonymous : user= User.objects.get(email='admin@admin.com')
    feedBack = FeedBack(user=user,feed = request.data['feed'])
    feedBack.save()
    return HttpResponse (json.dumps({"success":"success"}), content_type="application/json" , status=status.HTTP_200_OK)


@api_view(['Get'])
@permission_classes([AllowAny])
def getFeeds(request):
    feeds = FeedBack.objects.all()
    return HttpResponse (serializers.serialize('json',feeds), content_type="application/json" , status=status.HTTP_200_OK)
