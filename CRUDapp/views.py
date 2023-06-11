from django.shortcuts import render
from .serializers import Student ,StudentInfo , StudentUpdate,studentdelete,StudentInfoView
from .query import studentdata__q ,studentViewdata_q,studentUpdtedata_q,updatesavedata_q,studentdelete_q,all_studentdata_q
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.exceptions import APIException

from rest_framework.decorators import api_view

@api_view(['POST'])
def studentinfo_get(request):
    try:
        serializer=Student(data=request.data)
        
        if serializer.is_valid():

            Data={
                    "student_id":serializer.data['student_id'],
                    "student_name":serializer.data['student_name'],
                    "student_contact":serializer.data['student_contact'],
                    "student_age":serializer.data['student_age'],
                    "student_address":serializer.data['student_address']
                }
            userdata=studentdata__q(Data.values())
            print(userdata)


            if Data:
                g=serializer.data["student_id"]
                json_data = {
                    'status_code': 200,
                    'status':'Success',
                    'data':g,
                    'message': 'Data Inserted successfully',
                }
                return Response(json_data,status=status.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Failed',
                    'data':'',
                    'message': 'Data Insertion Failed',
                }
                return Response(json_data,status=status.HTTP_200_OK)

    
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=status.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data) 


@api_view(['Post'])
def student_view(request):
    try:
        serializer=StudentInfo(data=request.data)

        if serializer.is_valid():
            print("hello")
            student_id=serializer.data['student_id']
            Data=studentViewdata_q(student_id)
            
            if Data:
                json_data = {
                    'status_code': 200,
                    'status':'Success',
                    'data':Data,
                    'message': 'Data Inserted successfully',
                }
                return Response(json_data,status=status.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Failed',
                    'data':'',
                    'message': 'Data Insertion Failed',
                }
                return Response(json_data,status=status.HTTP_200_OK)

    
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=status.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 500,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data) 

@api_view(['POST'])
def student_update(request):
    try:
        serializer=StudentUpdate(data=request.data)

        if serializer.is_valid():
             print("hello")
             uuid=serializer.data['studentUUID']
             data=studentUpdtedata_q(uuid)
             Data={
                    "student_id":serializer.data['student_id'] if serializer.data['student_id'] else data['student_id'],
                    "student_name":serializer.data['student_name'] if serializer.data['student_name'] else data['student_name'],
                    "student_contact":serializer.data['student_contact'] if serializer.data['student_contact'] else data['student_contact'],
                    "student_age":serializer.data['student_age'] if serializer.data['student_age'] else data['student_age'],
                    "student_address":serializer.data['student_address'] if serializer.data['student_address'] else data['student_address'],
                    "studentUUID":serializer.data['studentUUID']
                }
             newdata=updatesavedata_q(Data.values())
             
             if newdata:
                json_data = {
                    'status_code': 200,
                    'status':'Success',
                    'data':'',
                    'message': 'Data Inserted successfully',
                }
                return Response(json_data,status=status.HTTP_200_OK)
             else:
                json_data = {
                    'status_code': 200,
                    'status': 'Failed',
                    'data':'',
                    'message': 'Data Insertion Failed',
                }
                return Response(json_data,status=status.HTTP_200_OK)

    
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=status.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 500,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data) 

@api_view(['POST'])
def student_delete(request):
    try:
        serializer=studentdelete(data=request.data)
        print("hello")
        if serializer.is_valid():
            uuid=serializer.data['studentUUID']
            data=studentdelete_q(uuid)


            if data:
                json_data = {
                    'status_code': 200,
                    'status':'Success',
                    'data':'',
                    'message': 'Data  deleted',
                }
                return Response(json_data,status=status.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Failed',
                    'data':'',
                    'message': 'Data deletioin Failed',
                }
                return Response(json_data,status=status.HTTP_200_OK)

    
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=status.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 500,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data) 


@api_view(['POST'])
def getstudentList(request):
    try:
        serializer=StudentInfoView(data=request.data)
        print("hello")
        if serializer.is_valid():
            data=all_studentdata_q()
            if data:
                json_data = {
                    'status_code': 200,
                    'status':'Success',
                    'data':data,
                    'message': 'Data  deleted',
                }
                return Response(json_data,status=status.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Failed',
                    'data':'',
                    'message': 'NO Data available ',
                }
                return Response(json_data,status=status.HTTP_200_OK)

    
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=status.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 500,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data) 
        
    #     data=all_studentdata_q()
    #     if data:
    #             json_data = {
    #                 'status_code': 200,
    #                 'status':'Success',
    #                 'data':'',
    #                 'message': 'Data  deleted',
    #             }
    #             return Response(json_data,status=status.HTTP_200_OK)
    #         else:
    #             json_data = {
    #                 'status_code': 200,
    #                 'status': 'Failed',
    #                 'data':'',
    #                 'message': 'Data deletioin Failed',
    #             }
    #             return Response(json_data,status=status.HTTP_200_OK)

    
    #     else:
    #         json_data = {
    #             'status_code': 300,
    #             'status': 'Fail',
    #             'Reason': serializer.errors,
    #             'Remark': 'Send valid data'
    #         }
    #         return Response(json_data, status=status.HTTP_300_MULTIPLE_CHOICES)
    # except Exception as e:
    #     print("Error --------:", e)
    #     json_data = {
    #         'status_code': 500,
    #         'status': 'Fail',
    #         'Reason': e,
    #         'Remark': 'landed in exception',
    #     }
    #     raise APIException(json_data) 








        


