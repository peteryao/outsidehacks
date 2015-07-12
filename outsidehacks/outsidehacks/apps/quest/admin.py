from django.contrib import admin

from .models import Zone, Badge, Quest, UserQuest, UserBadge

admin.site.register(Zone)
admin.site.register(Badge)
admin.site.register(Quest)
admin.site.register(UserQuest)
admin.site.register(UserBadge)