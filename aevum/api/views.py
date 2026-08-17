from rest_framework import permissions, response, viewsets, views
from hub.models import CodeSnippet, Event, Note, Tag, Task
from .serializers import CodeSnippetSerializer, EventSerializer, NoteSerializer, TagSerializer, TaskSerializer


class UserFilteredQuerySetMixin:
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(UserFilteredQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tag.objects.all()
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']


class NoteViewSet(UserFilteredQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Note.objects.prefetch_related('tags').all()
    search_fields = ['title', 'content']
    ordering_fields = ['updated_at', 'created_at', 'title']


class TaskViewSet(UserFilteredQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at']


class EventViewSet(UserFilteredQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    filterset_fields = ['is_public']
    search_fields = ['title', 'description']
    ordering_fields = ['start_date', 'created_at']


class CodeSnippetViewSet(UserFilteredQuerySetMixin, viewsets.ModelViewSet):
    serializer_class = CodeSnippetSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CodeSnippet.objects.all()
    filterset_fields = ['language', 'is_public', 'github_uploaded']
    search_fields = ['title', 'content']
    ordering_fields = ['updated_at', 'created_at']


class StatsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        data = {
            'notes': Note.objects.filter(user=request.user).count(),
            'tasks_todo': Task.objects.filter(user=request.user, status='todo').count(),
            'tasks_doing': Task.objects.filter(user=request.user, status='doing').count(),
            'tasks_done': Task.objects.filter(user=request.user, status='done').count(),
            'events': Event.objects.filter(user=request.user).count(),
            'snippets': CodeSnippet.objects.filter(user=request.user).count(),
            'github_uploaded': CodeSnippet.objects.filter(user=request.user, github_uploaded=True).count(),
        }
        return response.Response(data)
