from django.contrib import admin

# Register your models here.
from .models import Note
from .models import RegisterToken
from .models import CurrentNote

admin.site.register(Note)
admin.site.register(RegisterToken)
admin.site.register(CurrentNote)