from blessings import Terminal

t = Terminal()

def say_hello(name=None):
    if name is None:
        return "Hello, World!"
    else:
        return f"Hello, {t.red}{name}{t.normal}!"
