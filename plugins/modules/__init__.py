import os, sys, importlib, logging

base_dir = os.path.dirname(os.path.abspath("plugins/modules"))

def handlers():
  hlist = []
  help = {}
  for root, _, files in os.walk(base_dir):
    for file in files:
      if file.endswith(".py") and not file.startswith("_"):
        rel_path = os.path.relpath(os.path.join(root, file), base_dir).replace(os.sep, ".")[:-3]
        module = f"{os.path.basename(base_dir)}.{rel_path}"
        mod = importlib.import_module(module)
        if not mod:
          continue
        if x := getattr(mod, "__handlers__", False):
            hlist.extend(x)
        if hasattr(mod, "__mod__"):
          if hasattr(mod, "__help__"):
            help[mod.__mod__.lower()] = mod
  return hlist, help
  
HANDLERS, HELP = handlers()