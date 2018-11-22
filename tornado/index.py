import tornado.ioloop
import tornado.web


class handler(tornado.web.RequestHandler):
    def get(self):
        self.write(self.settings)

if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/',handler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

