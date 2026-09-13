import os
import django
from django.db.models.deletion import ProtectedError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from library.models import Author, Book

def run():
    print("--- PRUEBA CON on_delete=PROTECT ---")
    author = Author.objects.filter(books__isnull=False).first()
    if author:
        print(f"Autor a intentar borrar: {author} (Libros asociados: {author.books.count()})")
        try:
            author.delete()
            print("¡Error! Se borró el autor a pesar de PROTECT.")
        except ProtectedError as e:
            print("¡Comportamiento correcto con PROTECT!")
            print(f"Excepción capturada exitosamente: {e}")
            print(f"Los libros del autor siguen intactos. Total de libros en la BD: {Book.objects.count()}")
    else:
        print("No se encontró ningún autor con libros.")

if __name__ == '__main__':
    run()
