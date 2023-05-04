import importlib
from common import utils

# TODO Rename the package
utils.unload_packages(silent=True, package="template")
importlib.import_module("template")
# TODO rename app
from template.MayaTool import MayaTool
try:
    app.close()
except:
    pass
app = MayaTool()
app.show()
