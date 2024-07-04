from django.contrib import admin

from .models import Pereval, User, Coord, Level, PerevalImages

# Регистрация моделей
admin.site.register(Pereval)
admin.site.register(User)
admin.site.register(Coord)
admin.site.register(Level)
admin.site.register(PerevalImages)