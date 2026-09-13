import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from library.models import Author, AuthorProfile, Category, Publisher, Book, Publication

def run():
    print("Cargando datos de prueba...")

    # Limpiar datos anteriores (opcional, para idempotencia)
    Publication.objects.all().delete()
    Book.objects.all().delete()
    Publisher.objects.all().delete()
    Category.objects.all().delete()
    AuthorProfile.objects.all().delete()
    Author.objects.all().delete()

    # 1. Crear 3 Categorías
    c1 = Category.objects.create(name="Fisiología", description="Libros sobre fisiología y funcionamiento biológico.")
    c2 = Category.objects.create(name="Programación", description="Libros sobre desarrollo de software y lenguajes.")
    c3 = Category.objects.create(name="Historia", description="Libros de historia mundial y local.")
    print("Categorías creadas:", Category.objects.count())

    # 2. Crear 2 Editoriales (Publishers)
    pub1 = Publisher.objects.create(name="Editorial Tecnos", address="Calle Mayor 12", country="España")
    pub2 = Publisher.objects.create(name="O'Reilly Media", address="1005 Gravenstein Highway North", country="Estados Unidos")
    print("Editoriales creadas:", Publisher.objects.count())

    # 3. Crear 2 Autores con sus Perfiles
    author1 = Author.objects.create(first_name="Alan", last_name="Turing", email="alan@example.com")
    AuthorProfile.objects.create(
        author=author1,
        biography="Matemático, lógico y científico de la computación británico.",
        birth_date=date(1912, 6, 23),
        website="https://en.wikipedia.org/wiki/Alan_Turing"
    )

    author2 = Author.objects.create(first_name="Marie", last_name="Curie", email="marie@example.com")
    AuthorProfile.objects.create(
        author=author2,
        biography="Física y química polaca, pionera en el campo de la radiactividad.",
        birth_date=date(1867, 11, 7),
        website="https://en.wikipedia.org/wiki/Marie_Curie"
    )
    print("Autores creados:", Author.objects.count())

    # 4. Crear 4 Libros
    book1 = Book.objects.create(
        title="Computing Machinery and Intelligence",
        summary="Articulo pionero sobre inteligencia artificial.",
        author=author1
    )
    book1.categories.add(c2, c3) # Libro en dos categorías (Programación e Historia)

    book2 = Book.objects.create(
        title="Radioactive Substances",
        summary="Estudio detallado sobre elementos radiactivos.",
        author=author2
    )
    book2.categories.add(c1)

    book3 = Book.objects.create(
        title="The Annotated Turing",
        summary="Una guía guiada a través del articulo seminal de Turing.",
        author=author1
    )
    book3.categories.add(c2)

    book4 = Book.objects.create(
        title="Researches on Radioactive Substances",
        summary="Tesis doctoral sobre sustancias radiactivas.",
        author=author2
    )
    book4.categories.add(c1, c3) # Libro en dos categorías (Fisiología/Ciencia e Historia)

    print("Libros creados:", Book.objects.count())

    # 5. Crear publicaciones (modelo intermedio con Publisher, fecha y edición)
    Publication.objects.create(book=book1, publisher=pub2, publication_date=date(1950, 10, 1), edition=1)
    Publication.objects.create(book=book2, publisher=pub1, publication_date=date(1904, 5, 12), edition=1)
    Publication.objects.create(book=book3, publisher=pub2, publication_date=date(2008, 4, 15), edition=2)
    Publication.objects.create(book=book4, publisher=pub1, publication_date=date(1903, 1, 1), edition=1)

    print("Publicaciones creadas:", Publication.objects.count())
    print("¡Datos de prueba cargados exitosamente!")

if __name__ == '__main__':
    run()
