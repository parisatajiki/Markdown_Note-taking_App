import markdown
import language_tool_python
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from note_app.models import Note
from note_app.serializer import NoteSerializer


class GetNotes(APIView):
    def post(self, request):
        data = request.data.copy()

        if 'file' in data and data['file']:
            uploaded_file = data['file']
            content = uploaded_file.read().decode('utf-8')
            data['content'] = str(content)
        else:
            data['content'] = data.get('content', '')
            data['file'] = None

        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowNotes(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(instance=notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RenderNoteHTML(APIView):
    def get(self, request,pk=None):
        note = Note.objects.get(id=pk)
        note_html = markdown.markdown(note.content)
        return Response(note_html, status=status.HTTP_200_OK)




