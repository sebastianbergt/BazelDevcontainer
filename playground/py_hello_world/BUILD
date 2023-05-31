py_library(
    name = "hello_world",
    srcs = ["hello_world.py"],
    visibility = ["//visibility:public"]
)

py_test(
    name = "hello_world_test",
    srcs = ["hello_world_test.py"],
    deps = [
        "//playground/py_hello_world:hello_world"
    ],
)