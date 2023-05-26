from rest_framework import serializers
from .models import Admin, Person, Actives, Reports

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin 
        fields = ('admin_id', 'email', 'password')

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person 
        fields = ('person_id', 'rfid', 'name', 'lastname', 'phone')

class ActiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actives 
        fields = ('rfid', 'person', 'name', 'start_hour', 'finish_hour')

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reports 
        fields = ('report_id', 'person', 'name', 'report_date', 'start_hour', 'finish_hour')
