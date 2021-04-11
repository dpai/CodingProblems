#include <catch2/catch.hpp>
#include <vector>
using namespace std;

int FindInversions(const vector<int>& arr);

TEST_CASE( "2: Factorial of 0 is 1 (fail)", "[multi-file:2]" ) {
    REQUIRE( FindInversions({5,4,3,2,1}) == 10);
}