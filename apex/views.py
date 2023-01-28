from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.db import connection
# from django.db.models import Q
from datetime import date

from .helpers import validate_is_date
from .models import PatProfile, OpdRecord
from .serializers import PatProfileSerializer, OpdRecordSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Home' : '/'
    }
    return Response(api_urls)

@api_view(['GET'])
def index(request):
    return HttpResponse("Working... It is deployed! voila!")
        
    

@api_view(['GET'])
def return_search_results(request, field, value):
    try:
        final_field = field + '__' + 'icontains'
        res = PatProfile.objects.filter(**{ final_field : value })
        serializer = PatProfileSerializer(res, many=True)
    
        return JsonResponse(serializer.data, safe=False)
    
    except Exception as e:
        return Response(data=str(e), status=500)
    



@api_view(['GET'])
def return_day_opd(request, from_date=date.today(), to_date=date.today()):
    if (validate_is_date(from_date) and validate_is_date(to_date)):
        try:
            temp = []
        
            res = OpdRecord.objects.filter(date__range=(from_date, to_date))
        
            for e in res.select_related('ref'):
                temp.append(e.ref)
            
            serializer = PatProfileSerializer(temp, many=True)
            serializer2 = OpdRecordSerializer(res, many=True)
        
            for index, each in enumerate(serializer.data):
                each.update(serializer2.data[index])
        
            return JsonResponse(serializer.data, safe=False)

            # return Response(data={"res" : serializer.data}, status=200)
        except Exception as e:
          return Response(data={"res" : str(e)}, status=500)
        
    else:
          return Response(data={"res" : "URL validation failed, request denied"}, status=500)

    
@api_view(['GET'])
def return_profile(request, uid):
    data = []
    res1 = PatProfile.objects.get(pk = uid)
    res2 = OpdRecord.objects.filter(ref = uid)
    serializer1 = PatProfileSerializer(res1, many=False)
    serializer2 = OpdRecordSerializer(res2, many=True)
    
    data.append(serializer1.data)
    data.append(serializer2.data)
    return JsonResponse(data, safe=False)


@api_view(['POST'])
def create_profile(request):
    uid = request.data['uid']
    f_name = request.data['f_name']
    l_name = request.data['l_name']
    dob = request.data['dob']
    parent_name = request.data['parent_name']
    phone = request.data['phone']
    sex = request.data['sex']
    address = request.data['address']
    referred_by = request.data['referred_by']
    created_at = request.data['created_at']
    
    try:
        PatProfile.objects.create(uid=uid, f_name=f_name, l_name=l_name, dob=dob, parent_name=parent_name, phone=phone, sex=sex, address=address, referred_by=referred_by, created_at=created_at)
        return Response(data={"res" : "SUCCESS"}, status=200)
    except Exception as e:
        print(e)
        return Response(data={"res" : e}, status=500)
    

@api_view(['POST'])
def create_opd(request):
    date = request.data['date'],
    date_str = ''.join(date)
    charge = request.data['charge']
    height = request.data['height']
    weight = request.data['weight']
    temp = request.data['temp']
    ref = request.data['ref']
    try:
        res = OpdRecord.objects.create(date=date_str, charge=charge, height=height, weight=weight,temp=temp, ref=ref)
        newly_added = OpdRecord.objects.get(pk = res.id)
        serializer = OpdRecordSerializer(newly_added, many=False)

        return JsonResponse(data=serializer.data, safe=False)
    except Exception as e:
        return Response(data={"res" : e}, status=500)

@api_view(['POST'])
def update_opd_record(request):
      try:
        id_to_update = request.data['id']
        element_to_update = request.data['element']
        value_to_update = request.data['value']
        
        res2 = OpdRecord.objects.get(pk = id_to_update)
        setattr(res2, element_to_update, value_to_update)
        res2.save()
        serializer2 = OpdRecordSerializer(res2, many=False)
        updated_record = serializer2.data[element_to_update]
        return Response(data={"res" : {element_to_update : updated_record}}, status=200)
    
      except Exception as e:
        return Response(data={"res" : e}, status=500)