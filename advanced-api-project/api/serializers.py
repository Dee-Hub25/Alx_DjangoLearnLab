# api/serializers.py
from datetime import date
from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.

    Custom validation:
    - publication_year must not be in the future.
    """
    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

    def validate_publication_year(self, value: int) -> int:
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        if value < 0:
            raise serializers.ValidationError(
                "Publication year must be a positive integer."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Includes the author's name and a nested, read-only list of their books.

    Relationship handling:
    - We use the `related_name='books'` defined on Book.author, so we can declare
      `books = BookSerializer(many=True, read_only=True)`.
    - This dynamically serializes all Book instances related to an Author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
