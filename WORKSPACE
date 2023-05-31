load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Skylib
http_archive(
    name = "bazel_skylib",
    sha256 = "66ffd9315665bfaafc96b52278f57c7e2dd09f5ede279ea6d39b2be471e7e3aa",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
    ],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

bazel_skylib_workspace()


# Python
http_archive(
    name = "rules_python",
    sha256 = "8c8fe44ef0a9afc256d1e75ad5f448bb59b81aba149b8958f02f7b3a98f5d9b4",
    strip_prefix = "rules_python-0.13.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.13.0.tar.gz",
)

load("@rules_python//python:pip.bzl", "pip_install")
 
pip_install(
   name = "python_deps",
   requirements = "//third_party:requirements.txt",
)

# Catch2
http_archive(
    name = "com_github_catchorg_catch2",
    urls = ["https://github.com/catchorg/Catch2/archive/refs/tags/v3.3.2.tar.gz"],
    strip_prefix = "Catch2-3.3.2",
    sha256 = "8361907f4d9bff3ae7c1edb027f813659f793053c99b67837a0c0375f065bae2",
)
