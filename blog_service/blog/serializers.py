from rest_framework import serializers
from .models import Post
import requests

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_id', 'author', 'created_at']

    def get_author(self, obj):
        try:
            response = requests.get(f"http://127.0.0.1:5001/users/{obj.author_id}")
            if response.status_code == 200:
                return response.json()
        except:
            return {"error": "Author service unavailable"}
        return {"error": "Author not found"}