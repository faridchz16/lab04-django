from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    biography = models.TextField()
    birth_date = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil de Autor'
        verbose_name_plural = 'Perfiles de Autores'

    def __str__(self):
        return f"Perfil de {self.author}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    cover = models.ImageField(upload_to='books/', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')
    publishers = models.ManyToManyField(Publisher, through='Publication', related_name='books_published')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title']

    def __str__(self):
        return self.title


class Publication(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    edition = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        unique_together = ('book', 'publisher')

    def __str__(self):
        return f"{self.book} - {self.publisher} (Ed. {self.edition})"
