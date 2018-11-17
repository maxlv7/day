import contextlib

@contextlib.contextmanager
def file_open():
    print("file open")
    yield 123
    print("file end ")

with file_open() as f:
    print(f)
    print("file processed")