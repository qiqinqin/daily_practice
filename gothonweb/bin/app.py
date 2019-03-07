#coding=utf-8
import web
#正则表达式匹配URL，希望URL由名为Index的类处理
urls = (
	'/hello','Index'
)
app = web.application(urls,globals())
render = web.template.render('templates/',base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody",greet="Hello")
        greeting = "%s,%s"%(form.greet,form.name)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()

