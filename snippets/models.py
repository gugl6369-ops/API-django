from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted( [(item[1][0], item[0]) for item in LEXERS ] )
STYLE_CHOICES = sorted( [(item, item) for item in get_all_styles()] )

class Category (models.Model):
    name = models.CharField(max_length=100)

class Author (models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    biography = models.TextField(max_length=10000)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True)

    class Meta:
        ordering = ['name', 'surname', ]

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    date = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publishing = models.CharField(max_length=100)
    image = models.ImageField()
    file = models.FileField()



    # def save(self, *args, **kwargs):
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super(Snippet, self).save(*args, **kwargs)

    class Meta:
        unique_together = ['title', 'author', 'date', 'publishing']
        ordering = ['title', 'author']
