import platform
import os
import shutil

from test.examples_tools import chdir, run

def run_example(output_folder=""):

    if os.path.exists("build"):
        shutil.rmtree("build")

    run(f"conan install . {output_folder} --build missing")

    build_path = "build" if output_folder else "build/Release"
    gen_folder = "" if output_folder else "generators/"
    cmakelists_path = ".." if output_folder else "../.."
    with chdir(build_path):
        command = []
        # in the conanfile.py we only add CMake as tool_require in Linux
        command.append(f". ./{gen_folder}conanbuild.sh")
        command.append(f"cmake {cmakelists_path} -DCMAKE_TOOLCHAIN_FILE={gen_folder}conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release")
        command.append("cmake --build .")
        command.append(f". ./{gen_folder}deactivate_conanbuild.sh")
        run(" && ".join(command))
        cmd_out = run("./compressor")

    assert "ZLIB VERSION: 1.2.11" in cmd_out


print("- Understanding the flexibility of using conanfile.py vs conanfile.txt -")

# first run the basic example without layout and conditionals 

run_example(output_folder="--output-folder=build")