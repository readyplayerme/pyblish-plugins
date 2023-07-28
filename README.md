# Ready Player Me Pyblish Plugins

Pyblish plugins for Ready Player Me asset validation within 3D content creation software.

Currently only Blender is supported.
If you're looking for a convenient way to use these plugins, please check out the [Ready Player Me Blender Asset Validator](https://github.com/readyplayerme/blender-asset-validator) instead.  
This package is intended for developers who want to integrate the validation into their own pipeline.

## Installation

### Blender

We don't want to have to deal with file access permissions, so it's best to install the plugins in a user directory.
Blender's Python API can be used to find its user scripts directory with `bpy.utils.script_path_user()`.  
The directory can contain an _addons/modules/_ folder which will be added to Python's `sys.path`, according to [Blender’s directory layout](https://docs.blender.org/manual/en/latest/advanced/blender_directory_layout.html).
Here's an example script to install the plugins that can be run from within Blender or using a Python environment with Blender as a Python module (bpy) installed.

```python
import importlib
import subprocess
import sys
from pathlib import Path

import bpy

# Define the remote address to get the package from.
remote_path = "https://github.com/readyplayerme/pyblish-plugins/archive/main.zip"

# Define the path to the user script's folder and make sure it exists.
local_path = Path(bpy.utils.script_path_user()) / "addons" / "modules"
local_path.mkdir(parents=True, exist_ok=True)

# Install the package from the remote repository.
python_binary = sys.executable
# Installing the package also installs dependencies, so it takes a while.
subprocess.run([python_binary, "-m", "pip", "install", "--target", str(local_path), remote_path])

# Make blender reload the script paths to include our newly installed package.
importlib.invalidate_caches()
bpy.ops.script.reload()
```

## Usage

```python
import importlib.util
from pathlib import Path

import pyblish.api
import pyblish.util

pyblish.api.register_host("blender")

# Find out where our plugins are.
plugins_module = "readyplayerme.pyblish_plugins"
module_spec = importlib.util.find_spec(plugins_module)
module_path = Path(module_spec.origin).resolve().parent

# Register the plugins with pyblish.
pyblish.api.register_plugin_path(module_path)
plugins = pyblish.api.discover()
context = pyblish.util.collect(plugins=plugins)
context = pyblish.util.validate(context=context, plugins=plugins)

# Run auto-fix on all failed instances.
for plugin in plugins:
    try:
        if hasattr(plugin, "fix"):
            pyblish_action = plugin.fix
            pyblish_action.process(self=pyblish_action, context=context, plugin=plugin)
    except Exception as e:
        print(traceback.print_tb(e.__traceback__))
        print("failed to fix:", e)
```

The output of the validation is send to the console.
