from rest_framework import serializers


class TaskSerializer(serializers.Serializer):

    task_name = serializers.CharField(max_length=100)
    status = serializers.IntegerField()
    owner_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class SubTaskSerializer(serializers.Serializer):

    sub_task_name = serializers.CharField(max_length=100)
    task_id = serializers.IntegerField()
    created_date = serializers.DateTimeField()
    
    