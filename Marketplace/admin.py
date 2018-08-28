from django.contrib import admin

from .models import market, article, Liked, Comment, Internship, UserProfile, Friend, Workshop


#from Marketplace.forms import articleForm

admin.site.register(market)


admin.site.register(article)

admin.site.register(Liked)

admin.site.register(Comment)

admin.site.register(Internship)

admin.site.register(UserProfile)

admin.site.register(Friend)

admin.site.register(Workshop)

