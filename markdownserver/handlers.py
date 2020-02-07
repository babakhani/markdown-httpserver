from os.path import join, exists

from yhttp import Application, text, notfound, html

from .cli import Version
from .markdown import markdown2html
from . import indexer


app = Application()
app.cliarguments.append(Version)
app.settings.merge('''
root: .
html:
  header: <doctype><html><header></header><body>
  footer: </body></html>
''')


@app.route(r'/(.*)')
@html
def get(req, path):
    root = app.settings.root
    if not path:
        yield app.settings.html.header
        yield indexer.generate(root)
        yield app.settings.html.footer
        return

    filename = join(root, f'{path}.md')
    if not exists(filename):
        raise notfound()

    with open(filename) as f:
        yield app.settings.html.header
        yield markdown2html(f.read())
        yield app.settings.html.footer
