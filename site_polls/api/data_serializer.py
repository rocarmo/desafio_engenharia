from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    comments_qty = serializers.IntegerField
    comments_author = serializers.CharField
    comments_date = serializers.DateField

    # text1 = serializers.CharField(max_length=200)
    # text2 = serializers.CharField(max_length=200)

