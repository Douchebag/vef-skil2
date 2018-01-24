from bottle import route, run, static_file, request, error
import os

@error(404)
def error404(error):
    return "<h1>Þessi síða fannst ekki</h1>"

@route("/")
def index():
    return "<a href='/a'>Liður a</a> <a href='/b'>Liður b</a>"
@route("/a")
def a():
    return "<a href='/a/1'>Síða 1</a> <a href='/a/2'>Síða 2</a> <a href='/a/3'>Síða 3</a>"
@route("/a/<id>")
def about(id):
    return "<p>Þetta er síða " + id + "</p><a href='/a'>Til baka</a>"

@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root='./myndir')
@route("/b")
def b():
    return "<h2>Veldu þinn uppáhalds bókstaf</h2>"\
           "<a href='/result?mynd=a'><img src='/static/a.png'></a><a href='/result?mynd=b'><img src='/static/b.png'></a><a href='/result?mynd=c'><img src='/static/c.png'></a>"

@route("/result")
def result():
    mynd = request.query.mynd

    return '<h2>Þú valdir ' + mynd + '<h2>' \
            '<img src="/static/' + mynd + '.png">'


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))