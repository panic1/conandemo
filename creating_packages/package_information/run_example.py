import platform
import os

from test.examples_tools import run

print("- Define information for consumers depending on settings or options -")

out = run(f"conan create . --build=missing")

assertion = "Packaged 1 '.lib' file: hello-static.lib" if platform.system()=="Windows" else "Packaged 1 '.a' file: libhello-static.a"

assert assertion in out
