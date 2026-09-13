import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from library.models import Author, Book, Category, Publisher

def run():
    print("=== 1. CONSULTA DE IDA (libro.author) ===")
    book = Book.objects.first()
    print(f"Libro: '{book.title}'")
    print(f"Autor (ida): {book.author}")
    print(f"Email del autor: {book.author.email}\n")

    print("=== 2. CONSULTA DE VUELTA (autor.books.all()) ===")
    author = Author.objects.first()
    print(f"Autor: {author}")
    books = author.books.all()
    print(f"Libros del autor (vuelta):")
    for b in books:
        print(f" - {b.title}")
    print()

    print("=== 3. CONSULTA DE FILTRADO CON DOBLE GUION BAJO (__) ===")
    # Filtrar libros cuyo autor tenga apellido 'Turing'
    turing_books = Book.objects.filter(author__last_name='Turing')
    print("Libros cuyo autor tiene apellido 'Turing' (Book.objects.filter(author__last_name='Turing')):")
    for b in turing_books:
        print(f" - {b.title} (Autor: {b.author})")

    print("\nLibros pertenecientes a la categoría 'Programación' (Book.objects.filter(categories__name='Programación')):")
    prog_books = Book.objects.filter(categories__name='Programación')
    for b in prog_books:
        print(f" - {b.title}")

    print("\nAutores con perfil cuya fecha de nacimiento es anterior a 1900 (Author.objects.filter(profile__birth_date__year__lt=1900)):\n")
    old_authors = Author.objects.filter(profile__birth_date__year__lt=1900)
    for a in old_authors:
        print(f" - {a} (Nacimiento: {a.profile.birth_date})")

if __name__ == '__main__':
    run()
