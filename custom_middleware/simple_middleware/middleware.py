from django.http.response import HttpResponse
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        response = self.get_response(request)
        return response

        #print(requests.get("http://127.0.0.1:8000/project", headers={"x-endeavour-token":"authenticated"}))

    def process_view(self, request, view_func, view_args, view_kwargs):

        if "authenticated" not in request.headers['x-endeavour-token']:
            return HttpResponse(status=401)    
        pass

        