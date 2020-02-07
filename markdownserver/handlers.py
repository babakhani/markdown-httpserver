from os.path import join, exists

from yhttp import Application, text, notfound, html
from mako.template import Template

from .cli import Version
from .markdown import markdown2html
from . import indexer


app = Application()
app.cliarguments.append(Version)
app.settings.merge('''
root: .
''')
template = Template(filename='template.mako')


@app.route(r'/(.*)')
@html
def get(req, path):
    root = app.settings.root
    if not path:
        yield template.render(content=indexer.generate(root), settings=app.settings)
        return

    filename = join(root, f'{path}.md')
    if not exists(filename):
        raise notfound()

    with open(filename) as f:
        yield template.render(content=markdown2html(f.read()), settings=app.settings)
