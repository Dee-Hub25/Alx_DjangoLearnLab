# Delete Operation
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output:
# (1, {'bookshelf.Book': 1})
# <QuerySet []>
