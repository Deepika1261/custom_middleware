class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        response = self.get_response(request)
        return response

        #print(requests.get("http://127.0.0.1:8000/project", headers={"x-endeavour-token":"authenticated"}))

    def process_view(self, request, view_func, view_args, view_kwargs):
        
        if "authenticated" in request.headers['x-endeavour-token']:
            print("present")
            pass

        