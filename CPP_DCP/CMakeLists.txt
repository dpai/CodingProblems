## Setup minimum required version for CMake
cmake_minimum_required(VERSION 3.15)

project(DailyCoding CXX)

## Set C++ standard/compile-time options
add_library(project_options INTERFACE)
target_compile_features(project_options INTERFACE cxx_std_17)

option(ENABLE_TEST "Turn on to enable tests" ON )

if (ENABLE_TEST)
    enable_testing()

    # add catch as a single download into a directory. Rebasing would require deleting file from location
    # and running CMake
    if(NOT EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/import/downloads/catch2/catch.hpp)
       file(DOWNLOAD https://raw.githubusercontent.com/catchorg/Catch2/master/single_include/catch2/catch.hpp
               ${CMAKE_CURRENT_SOURCE_DIR}/import/downloads/catch2/catch.hpp)
    endif()
    set(CATCH2_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/import/downloads)

    add_library(Catch INTERFACE)
    target_include_directories(Catch INTERFACE ${CATCH2_INCLUDE_DIR})

    add_library(catch_main STATIC catch_main.cpp)
    target_link_libraries(catch_main PUBLIC Catch)
    target_link_libraries(catch_main PRIVATE project_options)
    #add_subdirectory(test)
endif()

## Problem Lists
add_subdirectory(Daily_18)
add_subdirectory(Daily_773)
add_subdirectory(Daily_854)

add_executable(Main main.cpp)
target_link_libraries(Main PRIVATE project_options)
target_link_libraries(Main PUBLIC daily_773)
target_link_libraries(Main PUBLIC daily_18)
target_link_libraries(Main PUBLIC daily_854)
