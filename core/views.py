import requests
from django.http import JsonResponse
from django.db.models import Count # We'll need this for the report
from django.shortcuts import render # And this

# ... (add these to existing imports)
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

# ... (This is your existing ViewSet)
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer

# ... (This is our new API integration view)
def fetch_external_articles(request):
    url = 'https://jsonplaceholder.typicode.com/posts?_limit=10' # Get 10 posts
    response = requests.get(url)
    data = response.json()

    articles_created_count = 0
    for item in data:
        # Use get_or_create to avoid duplicates
        article, created = Article.objects.get_or_create(
            external_id=item['id'],
            defaults={
                'title': item['title'],
                'content': item['body'],
                'author_name': f"User {item['userId']}" # Fake author name
            }
        )
        if created:
            articles_created_count += 1

    return JsonResponse({
        'status': 'success',
        'articles_created': articles_created_count
    })

def article_report(request):
    # Use the Django ORM to aggregate data
    data = Article.objects.values('author_name').annotate(count=Count('id')).order_by('-count')

    # Prepare data for Chart.js
    # We need two lists: labels (authors) and values (counts)
    labels = [item['author_name'] for item in data]
    values = [item['count'] for item in data]

    context = {
        'labels': labels,
        'values': values,
    }
    return render(request, 'core/report.html', context)