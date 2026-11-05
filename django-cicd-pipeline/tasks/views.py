import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Task


def health(request):
    return JsonResponse({"status": "ok"})


@csrf_exempt
@require_http_methods(["GET", "POST"])
def task_list(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body or "{}")
        except json.JSONDecodeError:
            return JsonResponse({"error": "invalid JSON"}, status=400)
        title = (payload.get("title") or "").strip()
        if not title:
            return JsonResponse({"error": "title is required"}, status=400)
        task = Task.objects.create(title=title)
        return JsonResponse({"id": task.id, "title": task.title, "done": task.done}, status=201)
    data = list(Task.objects.values("id", "title", "done"))
    return JsonResponse({"tasks": data})
