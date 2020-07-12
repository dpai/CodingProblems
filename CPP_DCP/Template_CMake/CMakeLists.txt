## Setup minimum required version for CMake
cmake_minimum_required(VERSION 3.15)

project(problem CXX)

## Set C++ standard/compile-time options
add_library(project_options INTERFACE)
target_compile_features(project_options INTERFACE cxx_std_17)

add_subdirectory(src)

option(ENABLE_TEST "Turn on to enable tests" ON)

if (ENABLE_TEST)
    enable_testing()
    add_library(Catch INTERFACE)
    target_include_directories(Catch INTERFACE ${PROJECT_SOURCE_DIR}/import/)
    add_subdirectory(test)
endif()