from os.path import join, exists, dirname

from yhttp import Application, text, notfound, html
from mako.template import Template
from mako.lookup import TemplateLookup

from .cli import Version
from .markdown import markdown2html
from . import indexer


app = Application()
app.cliarguments.append(Version)
app.settings.merge('''
root: .
templatedir: 'mako'
''')
templatelookup = TemplateLookup(
    directories=[join(dirname(__file__), app.settings.templatedir)],
    output_encoding='utf-8',
    encoding_errors='replace'
)
template = templatelookup.get_template("master.mako")


@app.route(r'/(.*)')
@html
def get(req, path):
    root = app.settings.root
    if not path:
        yield template.render(
            content=indexer.generate(root),
            settings=app.settings
        )
        return

    filename = join(root, f'{path}.md')
    if not exists(filename):
        raise notfound()

    with open(filename) as f:
        yield template.render(
            content=markdown2html(f.read()),
            settings=app.settings
        )
