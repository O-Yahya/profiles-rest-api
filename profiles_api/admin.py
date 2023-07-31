from django.contrib import admin
from profiles_api import models

# Registering created models to django admin
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
