from yhttp import Application

from .cli import Version


app = Application()
app.cliarguments.append(Version)


@app.route()
def get(req):
    return b'Hello World!'
