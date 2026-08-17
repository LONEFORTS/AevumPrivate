from django.contrib import admin
from .models import CodeSnippet, Event, FocusSession, Note, Profile, SharedLink, Tag, Task

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Note)
admin.site.register(Task)
admin.site.register(Event)
admin.site.register(CodeSnippet)
admin.site.register(FocusSession)
admin.site.register(SharedLink)
