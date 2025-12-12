from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


def health(request):
    return JsonResponse({"status": "ok", "service": "novya-backend"})


def favicon(request):
    return HttpResponse(status=204)



@api_view(['GET'])
@permission_classes([AllowAny])  # Temporary - remove authentication for testing
def get_classes(request):
    """
    Get available classes for the student
    """
    classes_data = [
        {
            "id": 1,
            "name": "Mathematics",
            "grade": "Grade 5", 
            "subject": "math",
            "color": "#FF6B6B",
            "icon": "calculator",
            "description": "Learn numbers, algebra, and geometry"
        },
        {
            "id": 2,
            "name": "Science",
            "grade": "Grade 5",
            "subject": "science",
            "color": "#4ECDC4",
            "icon": "flask", 
            "description": "Explore physics, chemistry, and biology"
        },
        {
            "id": 3,
            "name": "English",
            "grade": "Grade 5",
            "subject": "english",
            "color": "#45B7D1",
            "icon": "book",
            "description": "Improve reading, writing, and communication"
        }
    ]
    return Response(classes_data)



@api_view(['GET'])
@permission_classes([AllowAny])
def get_classes(request):
    """
    Get available classes for the student
    """
    classes_data = [
        {
            "id": 1,
            "name": "Mathematics",
            "grade": "Grade 5",
            "subject": "math",
            "color": "#FF6B6B",
            "icon": "calculator",
            "description": "Learn numbers, algebra, and geometry"
        },
        {
            "id": 2,
            "name": "Science",
            "grade": "Grade 5",
            "subject": "science",
            "color": "#4ECDC4",
            "icon": "flask",
            "description": "Explore physics, chemistry, and biology"
        },
        {
            "id": 3,
            "name": "English",
            "grade": "Grade 5",
            "subject": "english",
            "color": "#45B7D1",
            "icon": "book",
            "description": "Improve reading, writing, and communication"
        },
        {
            "id": 4,
            "name": "Social Studies",
            "grade": "Grade 5",
            "subject": "social",
            "color": "#96CEB4",
            "icon": "globe",
            "description": "Discover history, geography, and civics"
        }
    ]
    return Response(classes_data)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def get_classes(request):
    """
    Get available classes for the student
    """
    classes_data = [
        {
            "id": 1,
            "name": "Mathematics",
            "grade": "Grade 5",
            "subject": "math",
            "color": "#FF6B6B",
            "icon": "calculator",
            "description": "Learn numbers, algebra, and geometry"
        },
        {
            "id": 2,
            "name": "Science",
            "grade": "Grade 5",
            "subject": "science",
            "color": "#4ECDC4",
            "icon": "flask",
            "description": "Explore physics, chemistry, and biology"
        },
        {
            "id": 3,
            "name": "English",
            "grade": "Grade 5",
            "subject": "english",
            "color": "#45B7D1",
            "icon": "book",
            "description": "Improve reading, writing, and communication"
        }
    ]
    return Response(classes_data)
