from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Sections, ArticleSection, Article


class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_present = False
        for form in self.forms:
            is_main = form.cleaned_data.get('main_section', False)
            delete = form.cleaned_data.get('DELETE', False)
            if delete and is_main:
                raise ValidationError("ERROR! Это главная рубрика и её нельзя удалить!")
            if is_main_present and is_main:
                raise ValidationError("ERROR! Вы выбрали больше чем 2 главных рубрик!")
            elif is_main:
                is_main_present = True
        if not is_main_present:
            raise ValidationError("ERROR! не задано главная рубрика!")
        return super().clean()


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    extra = 1
    formset = ArticleSectionInlineFormset


class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleSectionInline,)


class SectionAdmin(admin.ModelAdmin):
    inlines = (ArticleSectionInline,)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Sections, SectionAdmin)
