from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

from js.bootstrap import bootstrap_css
from js.bootstrap import bootstrap_js
from js.wysihtml5 import wysihtml5

library = Library('bootstrap-wysihtml5', 'resources')

wysihtml5_css = Resource(
    library,
    'css/bootstrap-wysihtml5-0.0.2.css',
    depends=[bootstrap_css, ],
    )

wysihtml5_js = Resource(
    library,
    'js/bootstrap-wysihtml5-0.0.2.js',
    depends=[wysihtml5, bootstrap_js, ],
    minified='js/bootstrap-wysihtml5-0.0.2.min.js',
    )

bootstrap_wysihtml5 = Group([wysihtml5_css, wysihtml5_js])
