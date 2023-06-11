from django.db import connection , connections
from .helper import dictfetchone,dictfetchall




def studentdata__q(data):
    with connections["default"].cursor() as cursor:
        resp = cursor.execute("""INSERT INTO  CRUD.Student (student_id,
	student_name,
    student_contact,
    student_age ,
    student_address,
     studentUUID,
      IsDeleted )
         VALUES (%s, %s, %s, %s, %s,UUID());""",data )
    return resp

def studentViewdata_q(data):
    with connections["default"].cursor()  as cursor:
        resp=cursor.execute(f"""SELECT student_id,student_name,student_contact,
        student_age,student_address,studentUUID FROM CRUD.Student WHERE student_id='{data}' 
        and IsDeleted ='0' ;""")
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp 


def studentUpdtedata_q(data):
    with connections["default"].cursor()  as cursor:
        resp=cursor.execute(f"""SELECT student_id,student_name,student_contact,
        student_age,student_address,studentUUID FROM CRUD.Student WHERE studentUUID='{data}' 
        and IsDeleted ='0' ;""")
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp 

def updatesavedata_q(data):
    with connections["default"].cursor()  as cursor:
        resp=cursor.execute("""update CRUD.Student 
                            SET student_id= %s,student_name= %s,student_contact=%s,
        student_age= %s,student_address= %s Where studentUUID= %s ;""",data)
    return resp 

def studentdelete_q(data):
    with connections["default"].cursor()  as cursor:
        resp=cursor.execute("""update CRUD.Student SET IsDeleted ='1' WHERE studentUUID=%s""",[data])
    return resp 




def all_studentdata_q():
    with connections["default"].cursor() as cursor:
       resp=cursor.execute("""select * from CRUD.Student Where IsDeleted='0';""")
       if resp and cursor.rowcount:
              
              resp = dictfetchall(cursor)
       else:
            resp = None
    return resp 


# def all_studentdata_q():
#     with connections["default"].cursor()  as cursor:
#         resp=cursor.execute(f"""SELECT student_id,student_name,student_contact,
#         student_age,student_address,studentUUID FROM CRUD.Student WHERE  IsDeleted ='0' ;""")
#         if resp and cursor.rowcount:
#             resp = dictfetchall(cursor)
#         else:
#             resp = None
#     return resp 


