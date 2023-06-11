from rest_framework import serializers


class Student(serializers.Serializer):
    student_id=serializers.CharField(required=True)
    student_name=serializers.CharField(required=True)
    student_contact=serializers.CharField(required=True)
    student_age=serializers.CharField(required=True)
    student_address=serializers.CharField(required=True)

    class Meta:
        fields='__all__'


class StudentInfo(serializers.Serializer):
    student_id=serializers.CharField(required=True)

    class Meta:
        fields='__all__'


class StudentUpdate(serializers.Serializer):
    student_id=serializers.CharField(required=False,allow_blank=True,allow_null=True)
    student_name=serializers.CharField(required=False,allow_blank=True,allow_null=True)
    student_contact=serializers.CharField(required=False,allow_blank=True,allow_null=True)
    student_age=serializers.CharField(required=False,allow_blank=True,allow_null=True)
    student_address=serializers.CharField(required=False,allow_blank=True,allow_null=True)
    studentUUID=serializers.CharField(required=True)
    print("hii")

    class Meta:
        fields='__all__'

class studentdelete(serializers.Serializer):
    studentUUID=serializers.CharField(required=True)

    class Meta:
        fields='__all__'

class StudentInfoView(serializers.Serializer):
   

    class Meta:
        fields='__all__'


