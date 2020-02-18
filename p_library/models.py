from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=128)
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name

class Redaction(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    friend_to = models.ForeignKey('Friends', on_delete=models.PROTECT, null=True, blank=True,
                                  related_name='friends_books')
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    authors = models.ManyToManyField(
        Author,
        through='Inspiration',
        through_fields=('book', 'author'),
        related_name='author_book',
    )

    def __str__(self):
        return self.title

class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="inspired_works",
    )

class Friends(models.Model):
    full_name = models.CharField(max_length = 100,help_text="Полное имя друга")
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = ("Друг")
        verbose_name_plural = ("Друзья")