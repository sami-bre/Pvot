from django.contrib import admin
from . models import Question, Choice, Citizen

# Register your models here.
"""
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Citizen)
"""


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['english_question_text', 'amharic_question_text', 'oromic_question_text']}),
        ('Date information', {'fields': ['pub_date', 'dead_line'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('english_question_text', 'pub_date', 'dead_line')
    list_filter = ('pub_date',)
    search_fields = ('english_question_text', 'amharic_question_text', 'oromic_question_text')


class CitizenAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['first_name', 'last_name', 'voter_id']}),
    ]
    list_display = ('first_name', 'last_name', 'voter_id')
    list_filter = ('first_name',)
    search_fields = ('first_name', 'last_name',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Citizen, CitizenAdmin)

