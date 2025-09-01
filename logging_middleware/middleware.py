import datetime

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request
        with open("request_response.log", "a") as f:
            f.write(f"[{datetime.datetime.now()}] Request: {request.method} {request.path}\n")

        response = self.get_response(request)

        # Log response
        with open("request_response.log", "a") as f:
            f.write(f"[{datetime.datetime.now()}] Response: {response.status_code}\n")

        return response
