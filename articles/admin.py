from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTag


class TagsInLineReload(BaseInlineFormSet):
    tags_status_count = 0

    def clean(self):
        for form in self.forms:
            if self.tags_status_count > 1:
                # вызовом исключения ValidationError можно указать админке о наличие ошибки
                # таким образом объект не будет сохранен,
                # а пользователю выведется соответствующее сообщение об ошибке
                raise ValidationError('Ошибка! Выберите один основной раздел для статьи')
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main') == True:
                self.tags_status_count += 1
        return super().clean()  # вызываем базовый код переопределяемого метода


class TagsInLine(admin.TabularInline):
    model = ArticleTag
    extra = 3
    formset = TagsInLineReload


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [TagsInLine,]


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']