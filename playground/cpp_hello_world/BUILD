
cc_library(
    name = "hello_world",
    hdrs = ["hello_world.h"],
    srcs = ["hello_world.cc"],
)

cc_test(
    name = "hello_world_test",
    srcs = ["hello_world_test.cc"],
    deps = [
        "@com_github_catchorg_catch2//:catch2_main",
        "//playground/cpp_hello_world:hello_world",
    ],
)