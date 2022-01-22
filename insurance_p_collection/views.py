from django.shortcuts import render
from .models import Insurance_p_collection
from .serializer import Insurance_p_collectionSerializer
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.views import APIView

class Insurance_p_collectionAPI(APIView):
    def get(self, request,*args, **kwargs):
        resp={}
        stu=Insurance_p_collection.objects.all()
        serializer=Insurance_p_collectionSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request,*args,**kwargs):
        json_data=request.data
        serializer=Insurance_p_collectionSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_201_CREATED
            res['msg']="Data Created Successfully......"
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,*args, **kwargs):
        res={}
        json_data=request.data #json data
        if json_data:
            id=json_data.get('id')
            stu=Insurance_p_collection.objects.get(id=id)
            serializer=Insurance_p_collectionSerializer(stu,data=json_data)
            if serializer.is_valid():
                serializer.save()
                res['status'] = status.HTTP_201_CREATED
                res['msg']="Data Updated Successfully......"
                return Response(res,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            res["error"]="All fields are required"
            res["status"]=status.HTTP_400_BAD_REQUEST
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,*args, **kwargs):
        json_data=request.data #json data
        id=json_data.get('id')
        result=Insurance_p_collection.objects.get(id=id)
        serializer=Insurance_p_collectionSerializer(result,data=json_data,partial=True)#complex data
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_201_CREATED
            res['msg']="Data Updated Successfully......"
            return Response(res)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Insurance_p_collectionDelete(APIView):
        def delete(self, request,*args, **kwargs):
            res={}
            try:
                record=Insurance_p_collection.objects.filter(id=kwargs['pk']).first()
                if record is not None:
                    record.delete()
                    res["msg"]="data deleted"
                    res["status"]=status.HTTP_204_NO_CONTENT
                    return Response(res,status.HTTP_204_NO_CONTENT)
                res['msg']="Something Went wrong"    
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
            except:
                res['msg']="Something Went wrong"    
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
            
class Insurance_p_collectiongetspecificdetails(APIView):
        def get(self, request,*args, **kwargs):
            resp={}
            try:
                record=Insurance_p_collection.objects.filter(id=kwargs["pk"]).first()
                if record is not None:
                    serializer=Insurance_p_collectionSerializer(record)
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    resp['error']='Something Went wrong'
                    return Response(resp,status=status.HTTP_400_BAD_REQUEST)
            except:
                resp['error']='Something Went wrong'
                return Response(resp,status=status.HTTP_400_BAD_REQUEST) 
            
class Insurance_p_collectionDeleteAll(APIView):
    def delete(self, request,*args, **kwargs):
        resp={}
        try:
            record = Insurance_p_collection.objects.all()
            if record is not None:    
                for i in record:
                    # pass
                    i.delete()
                resp["msg"]="data deleted"
                resp["status"]=status.HTTP_204_NO_CONTENT
                return Response(resp,status.HTTP_204_NO_CONTENT)    
            else:
                resp['msg']="Something Went wrong"    
                return Response(resp,status=status.HTTP_400_BAD_REQUEST)    
        except:
            resp['msg']="Something Went wrong"    
            return Response(resp,status=status.HTTP_400_BAD_REQUEST) 