#include <catch2/catch_test_macros.hpp>
#include "hello_world.h"

TEST_CASE("Greeting")
{
  REQUIRE(greeting() == "Hello World!");
}