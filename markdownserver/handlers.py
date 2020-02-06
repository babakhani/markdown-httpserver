from os.path import join, exists

from yhttp import Application, text, notfound
import mistune

from .cli import Version


app = Application()
app.cliarguments.append(Version)
app.settings.merge('''
root: .
html:
  header: <doctype><html><header></header><body>
  footer: </body></html>
''')


@app.route(r'/(.*)')
@text
def get(req, path):
    filename = join(app.settings.root, path)
    if not exists(filename):
        raise notfound()

    with open(filename) as f:
        yield app.settings.html.header
        yield mistune.markdown(f.read())
        yield app.settings.html.footer
