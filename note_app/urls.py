from django.urls import path
from .views import GetNotes,ShowNotes,RenderNoteHTML,ViewNoteHTML




urlpatterns = [
    path('add',GetNotes.as_view(),name='notes'),
    path('list',ShowNotes.as_view(),name='show_notes'),
    path('render/<int:pk>',RenderNoteHTML.as_view(),name='render_notes'),
]