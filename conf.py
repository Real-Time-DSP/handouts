project = 'Handouts'

extensions = [
    "myst_nb",
    "sphinx_panels"
]

templates_path = ['_templates']

exclude_patterns = ['_build', "README.md"]

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_theme_options = {
    'page_width': '100%',
    'body_max_width': '960px',
    'nosidebar': True,
}


html_favicon = "_static/favicon.ico"
html_static_path = ['_static']

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

jupyter_execute_notebooks = "off"

def setup(app):
    app.add_css_file('theme.css')
