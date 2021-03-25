from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Sections(models.Model):
    title = models.CharField(max_length=225, verbose_name="Название")
    articles = models.ManyToManyField(Article, through="ArticleSection")

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name="article")
    section = models.ForeignKey(Sections,
                                on_delete=models.CASCADE,
                                )
    main_section = models.BooleanField(verbose_name="Главная рубрика")

    class Meta:
        unique_together = (('article', 'section'),)

    def __str__(self):
        return '{0}_{1}'.format(self.article, self.section)
