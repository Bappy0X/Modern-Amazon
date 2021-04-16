from importlib import import_module
from os import listdir, getcwd, path

blueprints = [
    import_module(f"app.blueprints.{i[:-3]}").bp 
    for i in listdir(path.dirname(__file__))
    if not i in ["__pycache__", "__init__.py"] 
        and i.endswith(".py")
]

# Maybe not the most pythonic way to do it - but I built it and I love it