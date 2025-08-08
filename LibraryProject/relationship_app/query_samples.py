# django-models/relationship_app/query_samples.py

import os
import django

# Configure Django settings (important for running standalone scripts)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_sample_queries():
    print("--- Running Sample Queries ---")

    # Clean up previous data (optional, for fresh runs)
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create some sample data
    author1 = Author.objects.create(name="Stephen King")
    author2 = Author.objects.create(name="J.K. Rowling")

    book1 = Book.objects.create(title="It", author=author1)
    book2 = Book.objects.create(title="The Shining", author=author1)
    book3 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author2)
    book4 = Book.objects.create(title="Fantastic Beasts", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book3) # Add books to the library
    library1.books.add(book2) # You can add them one by one too

    library2 = Library.objects.create(name="Community Library")
    library2.books.add(book3, book4)

    librarian1 = Librarian.objects.create(name="Alice Smith", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Johnson", library=library2)


    # Query 1: Query all books by a specific author.
    print("\n1. Books by Stephen King:")
    stephen_king_books = Book.objects.filter(author=author1) # or author__name="Stephen King"
    for book in stephen_king_books:
        print(f"- {book.title} (Author: {book.author.name})")

    # Using related_name from Author to Book
    print("\n1b. Books by J.K. Rowling (using related_name):")
    jk_rowling = Author.objects.get(name="J.K. Rowling")
    for book in jk_rowling.books.all(): # Accessing related books via 'books' related_name
        print(f"- {book.title}")


    # Query 2: List all books in a library.
    print("\n2. Books in Central Library:")
    central_library = Library.objects.get(name="Central Library")
    for book in central_library.books.all(): # Accessing related books via ManyToMany
        print(f"- {book.title}")

    print("\n2b. Books in Community Library:")
    community_library = Library.objects.get(name="Community Library")
    for book in community_library.books.all():
        print(f"- {book.title}")


    # Query 3: Retrieve the librarian for a library.
    print("\n3. Librarian for Central Library:")
    try:
        librarian_for_central = central_library.librarian # Accessing librarian via 'librarian' related_name
        print(f"- {librarian_for_central.name}")
    except Librarian.DoesNotExist:
        print("No librarian found for Central Library.")

    print("\n3b. Librarian for Community Library:")
    try:
        librarian_for_community = community_library.librarian
        print(f"- {librarian_for_community.name}")
    except Librarian.DoesNotExist:
        print("No librarian found for Community Library.")

    print("\n--- End of Sample Queries ---")

if __name__ == "__main__":
    run_sample_queries()