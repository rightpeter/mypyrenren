import tornado.ioloop
import tornado.web
import sys
import os

f = open("out.txt", "w+")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "text/plain")

	if (self.get_argument("username")):
		username = self.get_argument("username")

    	if (self.get_argument("passwd")):
		passwd = self.get_argument("passwd")
	
    	errno = os.system('python rp.py '+username+' '+passwd)
	print >> f, username, passwd, errno
	if (errno == 0):
		self.redirect('/login_success')
	else :
		self.redirect('/login_error')
    

class LoginSuccessHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("loginsuccess.html");

class LoginErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("loginfailed.html");

class OtherErrorHandler(tornado.web.RequestHandler):
    def get(self):
	self.render("othererror.html");

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
    (r"/login_success", LoginSuccessHandler),
    (r"/login_error", LoginErrorHandler),
    (r"/other_error", OtherErrorHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
