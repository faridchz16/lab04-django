import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from library.models import Author, Book

def run():
    print("--- PRUEBA CON on_delete=CASCADE ---")
    author = Author.objects.filter(books__isnull=False).first()
    if author:
        print(f"Autor a borrar: {author} (Libros asociados: {author.books.count()})")
        # Borramos el autor
        author_id = author.id
        author.delete()
        print(f"Autor {author_id} borrado exitosamente con CASCADE.")
        print(f"Libros restantes de ese autor: {Book.objects.filter(author_id=author_id).count()} (fueron eliminados en cascada).")
    else:
        print("No se encontró ningún autor con libros.")

if __name__ == '__main__':
    run()
