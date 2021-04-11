# Generic test that uses conan libs
add_library(daily_773 OBJECT findInversions.cpp)

target_include_directories(daily_773 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

target_link_libraries(
    daily_773
  PRIVATE project_options
)

if( MSVC )
    set_property( DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT daily_773 )
endif()

##### TESTS
message("This is " ${ENABLE_TEST})
if (ENABLE_TEST)
    add_executable(daily_773_tests tests.cpp)
    target_link_libraries(daily_773_tests PRIVATE project_options catch_main)
    target_link_libraries(daily_773_tests PUBLIC daily_773)

    add_test(NAME Daily773Test COMMAND daily_773_tests)
endif()