from rest_framework import serializers
from hub.models import CodeSnippet, Event, Note, Tag, Task


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'color', 'created_at', 'updated_at']


class NoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'attachment', 'is_pinned', 'is_public', 'tags', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'due_date', 'created_at', 'updated_at']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'color', 'is_public', 'created_at', 'updated_at']


class CodeSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSnippet
        fields = ['id', 'title', 'language', 'content', 'code_file', 'is_public', 'github_uploaded', 'github_url', 'created_at', 'updated_at']
