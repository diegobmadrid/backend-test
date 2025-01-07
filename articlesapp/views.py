from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

from articlesapp.models import Articles
from articlesapp.serializers import ArticleSerializer
@api_view(['POST'])
def save_article(request):
    try:
        data = request.data
        serialized_data = ArticleSerializer(data=data)
        if serialized_data.is_valid() is False:
            return JsonResponse(data=serialized_data.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serialized_data.validated_data
        title_validation = Articles.objects.filter(title=validated_data['title']).exists()
        if title_validation:
            return JsonResponse(data='Article already exists, title duplicated.', safe=False, status=status.HTTP_400_BAD_REQUEST)
        Articles.objects.create(**validated_data)
        return JsonResponse(data=None, safe=False, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse(data=str(e), safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_articles(request):
    try:
        category_filter = request.GET.get("category")
        author_filter = request.GET.get("author")
        articles = Articles.objects.all()
        if category_filter is not None:
            articles = articles.filter(category=category_filter)
        if author_filter is not None:
            articles = articles.filter(author=author_filter)
        articles_serialized = ArticleSerializer(articles, many=True).data
        return JsonResponse(data=articles_serialized, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse(data=str(e), safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
