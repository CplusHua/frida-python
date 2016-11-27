#
# Compile example.dylib like this:
# $ clang -Wall -pipe -Os -shared -o /Users/oleavr/.Trash/example.dylib example.c
#
# Then run:
# $ python inject_blob.py Twitter /Users/oleavr/.Trash/example.dylib
#

from __future__ import unicode_literals, print_function
import frida
import sys

def on_uninjected(id):
    print("on_uninjected id=%u" % id)

(target, library_path) = sys.argv[1:]

device = frida.get_local_device()
device.on("uninjected", on_uninjected)
id = device.inject_library_file(target, library_path, "example_main", "w00t")
print("*** Injected, id=%u -- hit Ctrl+D to exit!" % id)
sys.stdin.read()
