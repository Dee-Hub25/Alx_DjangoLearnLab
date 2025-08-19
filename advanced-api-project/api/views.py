from django.shortcuts import render

# Create your views here.
# File: advanced_api_project/api/views.py

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    """
    GET: Retrieve a list of all books
    Accessible by all users (read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book by ID
    Accessible by all users (read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    """
    POST: Add a new book
    Restricted to authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book
    Restricted to authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book
    Restricted to authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
