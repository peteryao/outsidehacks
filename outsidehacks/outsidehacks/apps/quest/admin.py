from django.contrib import admin

from .models import Zone, Badge, Cateogry, Quest, UserQuest, UserBadge

admin.site.register(Zone)
admin.site.register(Badge)
admin.site.register(Cateogry)
admin.site.register(Quest)
admin.site.register(UserQuest)
admin.site.register(UserBadge)