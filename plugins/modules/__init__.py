import os, sys, importlib, logging

HANDLERS: list = []
HELP = {}
base_dir = os.getcwd()

for root, _, files in os.walk(base_dir):
  for file in files:
    if file.endswith(".py") and not file.startswith("_"):
      rel_path = os.path.relpath(os.path.join(root, file), base_dir).replace(os.sep, ".")[:-3]
      module = f"{os.path.basename(base_dir)}.{rel_path}"
      mod = importlib.import_module(module)
      if not mod:
        continue
      if x := getattr(mod, "__handlers__", False):
          HANDLERS.extend(x)
      if hasattr(mod, "__mod__"):
        if hasattr(mod, "__help__"):
            HELP[mod.__mod__.lower()] = mod