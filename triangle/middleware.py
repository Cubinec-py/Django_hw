from triangle.models import Logs
from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):

    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.path.startswith('/admin/'):
            Logs.objects.create(path=request.path, method=request.method)
