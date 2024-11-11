from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .serializer import FoodSerializer,RestarentSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Restarent,Food
# Create your views here.

#>>>>>>>>>Django>>>>>>>>>>


def home(request):
       fdetails=Food.objects.filter(foodId=204).values()
       rdetails=Restarent.objects.filter(restarentId=101).values()
       return render(request,'home.html',{'fdetails':fdetails,'rdetails':rdetails})
def about(request):
       return render(request,'about.html')






####>>>>>>Displaying All Restarent Records<<<<<<<<<<<<<<<<<<<<

def displayAllRestarents(request):
        alldetails=Restarent.objects.all()
        return render(request,'displayAll.html',{"alldetails":alldetails})


@api_view(['GET'])
def displayRRREST(request):
       details=Restarent.objects.all()
       serializerdata=RestarentSerializer(details,many=True)
       return Response(serializerdata.data)








#>>>>>>>>>>>FINDING/GET THE RESTARENT RECORDS<<<<<<<<<<<<<<<<<<<<<<<


def findRestarent(request):
        getloc=request.GET.get('rloc')
        rDetails=Restarent.objects.filter(restarentLocation=getloc).values()
        return render(request,'findRestarent.html',{'rDetails':rDetails})
        

@api_view(['POST'])
def findRestarentREST(request):
       ID = request.data.get('restarentId')
       d=Restarent.objects.filter(restarentId=ID).values()
       if d:
              details=RestarentSerializer(d,many=True)
              return Response(details.data,status=status.HTTP_302_FOUND)
       else:
              return Response(status=status.HTTP_404_NOT_FOUND)







#>>>>>>>>>>>>>DISPLAY ALL FOOD RECORDS<<<<<<<<<<<<<<<<<<<


def displayFItems(request):
       allItems=Food.objects.all()
       return render(request,'displayFItems.html',{'allItems':allItems})


@api_view(['GET'])
def displayFRREST(request):
       details=Food.objects.all()
       serializerdata=FoodSerializer(details, many=True)
       return Response(serializerdata.data)







#>>>>>>>>>>>>GET/FIND/FETCH THE FOOD ITEMS>>>>>>>>>>>>>>>>>>>>>


def getFood(request):
       getFId=request.GET.get('fId')
       fDetails=Food.objects.filter(foodId=getFId).values()
       return render(request,'getFood.html',{'fDetails':fDetails})

@api_view(['POST'])
def getFoodREST(request):
       name=request.data.get('name')
       food=Food.objects.filter(foodName=name)
       details=FoodSerializer(food,many=True)
       if food:
              return Response(details.data,status=status.HTTP_200_OK)
       else:
              return Response(status=status.HTTP_404_NOT_FOUND)
       




#>>>>>>>>>>>>>>>>>>>>INSERTING RESTARENT NEW RECORDS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def rinput(request):
       return render(request,'rinput.html')



def insertRRecords(request):
       restarentidno=request.POST['restarentidno']
       rname=request.POST['restarentname']
       rlocation=request.POST['restarentlocation']
       restarent=Restarent(restarentId=restarentidno,restarentName=rname,restarentLocation=rlocation)
       restarent.save()
       return render(request,'rinput.html',{'message':'Data Saved Successfully'})

@api_view(['POST'])
def insertRRRest(request):
          data=RestarentSerializer(data=request.data)
          if data.is_valid():
                 data.save()
                 return Response(status=status.HTTP_201_CREATED)
          else:
                 return Response(status=status.HTTP_400_BAD_REQUEST)
          
       










#>>>>>>>>>>>DELATING RESTARENT RECORDS/DETAILS<<<<<<<<<<<<<<<<<<<<<<<<<<

def delateRData(request):
       return render(request,'delateRData.html')



def delateRRecords(request):
       rid=request.POST.get('rid')
       delateRdetails=Restarent.objects.filter(restarentId=rid).delete()
       return render(request,'delateRData.html',{'message':'Records Delated Successfully'})

def bdelate(request,restarentId):
       records=Restarent.objects.get(restarentId=restarentId)
       records.delete()
       return redirect('displayAllRestarents')



@api_view(['POST'])
def delateRRREST(request):
       rid=request.data.get('Id')
       if rid:
              rdelate=Restarent.objects.filter(restarentId=rid).delete()
             
              return Response( status=status.HTTP_200_OK)
             
       else:
              return Response(status=status.HTTP_404_NOT_FOUND)













#>>>>>>>>>>>>>>>>>>>INSERTING FOOD NEW ITEMS RECORDS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def insertFData(request):
       return render(request,'finput.html')


def insertFRecords(request):
       foodid=request.POST['FID']
       foodname=request.POST['FNAME']
       foodprice=request.POST['FPRICE']
       food=Food(foodId=foodid,foodName=foodname,foodPrice=foodprice)
       food.save()
       return render(request,'finput.html',{'message':'Data inserted successfully'})



@api_view(['POST'])
def insertFRREST(request):
       finsert=FoodSerializer(data=request.data)
       if finsert.is_valid():
              finsert.save()
              return Response(status=status.HTTP_201_CREATED)
       else:
              return Response(status=status.HTTP_400_BAD_REQUEST)











#>>>>>>>>>>>>>DELATING FOOD ITEMS >>>>>>>>>>>>>>>>>>>>>>>>>>>>

def delateFdata(request):
       return render(request,'delateFdata.html')


def delateFRecords(request):
       fid=request.POST.get('fid')
       delateFdetails=Food.objects.filter(foodId=fid).delete()
       return render(request,'delateFdata.html',{'message':'Food Item Delated Successfully'})


@api_view(['POST'])
def delateFRREST(request):
       id=request.data.get('id')
       if id:
              fdelate=Food.objects.filter(foodId=id).delete()
              return Response(status=status.HTTP_200_OK)
       else:
              return Response(status=status.HTTP_404_NOT_FOUND)
       














#>>>>>>>>>>>>>>>>>>>>UPDATING RESTARENT RECORDS/DATA >>>>>>>>>>>>>>>>>>>>>>>>>>>>

def uRData(request):
       return render(request,'uRData.html')

def updateRRecords(request,restarentId):
       RId=request.POST.get('urid')
       name=request.POST.get('rname')
       location=request.POST.get('rlocation')
       updateRRecords=Restarent.objects.filter(restarentId=RId).update(restarentName=name,restarentLocation=location)
       return render(request,'uRData.html',{'message':'Data Updated Successfully'})




def bupdate(request,restarentId):
       id=Restarent.objects.get(restarentId=restarentId)
       name=request.POST.get('rname')
       location=request.POST.get('rlocation')
       updateRRecords=Restarent.objects.filter(restarentId=restarentId).update(restarentName=name,restarentLocation=location)
       return render('bupdate.html',{'resatrentId':id})






@api_view(['POST'])
def updateRRREST(request):
       rid=request.data.get('id')
       rname=request.data.get('rname')
       rloc=request.data.get('rloc')
       if not rid:
              return Response({'error': 'Restaurant ID is required'}, status=status.HTTP_400_BAD_REQUEST)
       else:
              Restarent.objects.filter(restarentId=rid).update(restarentName=rname, restarentLocation=rloc)
              return Response(status=status.HTTP_200_OK)







#>>>>>>>>>>>>>>UPDATING FOOD ITEMS/RECORDS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def uFData(request):
       return render(request,'uFData.html')

def updateFRecords(request):
       FId=request.POST.get('ufid')
       fname=request.POST.get('fname')
       fprice=request.POST.get('fprice')
       Food.objects.filter(foodId=FId).update(foodName=fname,foodPrice=fprice)
       return render(request,'uFData.html',{'message':'Data Updated Successfully'})
              
    
@api_view(['POST'])
def updateFRREST(request):
       fid=request.data.get('fid')
       fname=request.data.get('fname')
       fprice=request.data.get('fprice')
       if fid:
              ufdetails=Food.objects.filter(foodId=fid).update(foodName=fname,foodPrice=fprice)
              return Response(status=status.HTTP_200_OK)
       else:
              return Response(status=status.HTTP_400_BAD_REQUEST)










