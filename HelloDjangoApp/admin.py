from django.contrib import admin
from HelloDjangoApp.models import Student, Subject


class SubjectInline(admin.TabularInline):   #admin.StackedInline
    model = Subject
    extra = 2


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['forename', 'surname']}),
        ('Birthday', {'fields': ['birth_day'], 'classes': ['collapse']})
    ]
    inlines = [SubjectInline]
    list_display = ('forename', 'surname', 'approximate_age')
    list_filter = ['forename', 'birth_day']
    search_fields = ['surname']
    date_hierarchy = 'birth_day'

admin.site.register(Student, StudentAdmin)
admin.site.register(Subject)
