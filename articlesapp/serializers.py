from rest_framework import serializers
from articlesapp.models import Articles
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
    category = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    class Meta:
        model = Articles
        fields = '__all__'