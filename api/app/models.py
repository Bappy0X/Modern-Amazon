class Reviews:
    def __iter__(self):
        yield "total", 123

class Category:
    def __iter__(self):
        yield "name", "In-Ear Headphones"
        yield "position", 4

class Categories:
    def __iter__(self):
        yield "bsr", dict(Category())

class Dimensions:
    def __iter__(self):
        yield "width", 12
        yield "height", 12
        yield "depth", 12
        yield "weight", 2.83
        yield "w", "g"
        yield "d", "cm"

class Product:
    def __iter__(self):
        yield "asin", "ASD"
        yield "title", "123"
        yield "images", ["https://example.com"]
        yield "price", 12.99
        yield "reviews", dict(Reviews())
        yield "categories", dict(Categories())
        yield "dimensions", dict(Dimensions())