from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
import json
from .models import ShortURL
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_short_url(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        url = data.get("url")
        validity = data.get("validity", 30)  # default = 30 mins
        shortcode = data.get("shortcode", None)

        if not url:
            return JsonResponse({"error": "URL is required"}, status=400)

        expiry_time = timezone.now() + timedelta(minutes=validity)

        obj = ShortURL.objects.create(
            url=url,
            shortcode=shortcode if shortcode else None,
            expiry=expiry_time
        )

        response = {
            "shortLink": f"http://localhost:8000/{obj.shortcode}",
            "expiry": expiry_time.isoformat()
        }
        return JsonResponse(response, status=201)

    return JsonResponse({"error": "Invalid request"}, status=400)
