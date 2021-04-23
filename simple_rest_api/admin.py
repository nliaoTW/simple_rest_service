from django.contrib import admin

from simple_rest_api import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
