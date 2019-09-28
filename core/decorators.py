import datetime
from functools import wraps
from django.utils import timezone

# def confirm_password(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         last_login = request.user.last_login
#         timespan = last_login + datetime.timedelta(hours=6)      
#         from core.views import confirmPassToContinue
#         return confirmPassToContinue.as_view()(request, *args, **kwargs)
#     return _wrapped_view