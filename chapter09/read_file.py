
def myRead(f,newline):
    buf = ''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos+len(newline):]
        chunk = f.read(1024)

        if not chunk:
            yield buf
            break
        buf+=chunk

with open('test.txt') as f:
    x = myRead(f,"{|}")
    print(next(x))
    print(next(x))
    print(next(x))