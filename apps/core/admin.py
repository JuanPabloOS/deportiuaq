from django.contrib import admin
from .models import User, Team, Workshop, TeamMember, WsMember, Match, Player
# Register your models here.

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Workshop)
admin.site.register(TeamMember)
admin.site.register(WsMember)
admin.site.register(Match)
admin.site.register(Player)