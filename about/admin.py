from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from about.models import About

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    
    def __str__(self):
        return self.title