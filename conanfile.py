from conan import ConanFile
from conan.tools.files import copy
import os


required_conan_version = ">=2.0"


boost_libs = [
    "atomic",
    "chrono",
    "container",
    "context",
    "contract",
    "coroutine",
    "date_time",
    "exception",
    "fiber",
    "filesystem",
    "graph",
    "iostreams",
    "json",
    "locale",
    "log_setup",
    "log",
    "math_c99f",
    "math_c99l",
    "math_c99",
    "math_tr1f",
    "math_tr1l",
    "math_tr1",
    "nowide",
    "prg_exec_monitor",
    "program_options",
    "python312",
    "random",
    "regex",
    "serialization",
    "stacktrace_noop",
    "stacktrace_windbg_cached",
    "stacktrace_windbg",
    "system",
    "test_exec_monitor",
    "thread",
    "timer",
    "type_erasure",
    "unit_test_framework",
    "url",
    "wave",
    "wserialization"
]


class BoostConan(ConanFile):
    name = "boost"
    version = "1.84.0"
    settings = "os", "arch", "compiler", "build_type"

    def layout(self):
        self.folders.build = "source"
        self.folders.source = self.folders.build

    def package(self):
        copy(self, "*",
            os.path.join(self.build_folder, "boost"),
            os.path.join(self.package_folder, "include", "boost"),
            keep_path=True)

        prefix = "libboost_"
        postfix = "-vc143-mt"

        if self.settings.build_type == "Debug":
            postfix = postfix + "-gd"

        postfix = postfix + "-x64-1_84.lib"

        for lib in boost_libs:
            libname = prefix + lib + postfix

            copy(self, libname,
                os.path.join(self.build_folder, "stage", "lib"),
                os.path.join(self.package_folder, "lib"),
                keep_path=False)

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "Boost")

        self.cpp_info.components["headers"].libs = []
        self.cpp_info.components["headers"].libdirs = []
        self.cpp_info.components["headers"].set_property("cmake_target_name", "Boost::headers")

        self.cpp_info.components["headers"].defines = [
            "BOOST_SYSTEM_NO_DEPRECATED",
            "BOOST_ASIO_NO_DEPRECATED",
            "BOOST_FILESYSTEM_NO_DEPRECATED",
            "BOOST_DLL_USE_STD_FS",
            "BOOST_SYSTEM_USE_UTF8",
            "BOOST_ALL_NO_LIB",
            "BOOST_PYTHON_STATIC_LIB"
        ]

        prefix = "libboost_"
        postfix = "-vc143-mt"

        if self.settings.build_type == "Debug":
            postfix = postfix + "-gd"

        postfix = postfix + "-x64-1_84"

        for lib in boost_libs:
            libname = prefix + lib + postfix

            self.cpp_info.components[lib].libs = [libname]
            self.cpp_info.components[lib].set_property("cmake_target_name", "Boost::" + lib)
            self.cpp_info.components[lib].requires = ["headers"]
