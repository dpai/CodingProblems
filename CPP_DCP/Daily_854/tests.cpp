#include <catch2/catch.hpp>
#include <vector>
#include <string>
using namespace std;

int splitlines(string &input, int idx, int k, vector<string>& result);

TEST_CASE( "2: Factorial of 0 is 1 (fail)", "[multi-file:2]" ) {
    REQUIRE( true);
}