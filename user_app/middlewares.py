from django.utils.deprecation import MiddlewareMixin
import time

class Logs(MiddlewareMixin):
    
    def process_request(self, request):
        request.request_time = time.time()
    
    def process_response(self, request, response):
        time_duration = time.time() - request.request_time
        print(f"time duration is: {time_duration}")
        return response