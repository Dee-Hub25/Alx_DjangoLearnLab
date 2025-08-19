# api/models.py
from django.db import models

class Author(models.Model):
    """
    Represents a writer/creator of one or more books.
    One Author -> Many Books (via Book.author FK).
    """
    name = models.CharField(
        max_length=255,
        help_text="Author's full name.",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    """
    Represents a single book written by an Author.
    `author` creates a one-to-many relationship (one Author, many Books).
    `related_name='books'` lets us access an author's books via `author.books`.
    """
    title = models.CharField(max_length=255, help_text="Book title.")
    publication_year = models.PositiveIntegerField(
        help_text="Four-digit year the book was published."
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        help_text="Link to the Author who wrote this book.",
    )

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return f"{self.title} ({self.publication_year})"
