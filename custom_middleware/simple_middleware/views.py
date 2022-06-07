from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.views import View

# Create your views here.
class ProjectView(View):

    def get(self, request: HttpRequest):

        return JsonResponse({"message":"Request successful"},status=200)

