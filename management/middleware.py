from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.contrib.sites.models import Site
from django.contrib.auth import logout
from django.contrib import messages
from django.http import Http404


class LastSeenMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.user.is_authenticated:
           user = request.user
           user.profile.last_seen = timezone.now()
           user.save()

        response = self.get_response(request)
        return response
    

class SiteMiddleware(MiddlewareMixin):

    def process_request(self, request):
        domain = request.get_host().split(':')[0]

        try:
            site = Site.objects.get(domain=domain)
            if request.user.is_authenticated:
                if site == request.user.profile.site:
                    request.team_id = request.user.profile.team_id
                    request.site = site
                else:
                    logout(request)
                    request.site = None
                    messages.error(request, "Invalid username or password.")
            else:
                request.site = site
                request.team_id = None
        except Site.DoesNotExist:
            request.site = None
            request.team_id = None
            if domain != "127.0.0.1":
                raise Http404('Site not found!')
                



    
