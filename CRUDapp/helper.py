import time, os

def dictfetchall(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

# def dictfetchall_new(cursor=''):
#     # "Returns all rows from a cursor as a dict"
#     desc = cursor.description
#     return [
#         dict(zip([col[0] for col in desc], row))
#         for row in cursor.fetchall()
#     ]
def dictfetchall_new(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    print("1111111111111111")
    z=[
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
    print(z)
    return z


def dictfetchone(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))