# Generic test that uses conan libs
add_library(daily_854 OBJECT breakstring.cpp)

target_include_directories(daily_854 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

target_link_libraries(
    daily_854
    PRIVATE project_options
)

if( MSVC )
    set_property( DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT daily_854 )
endif()

##### TESTS
if (ENABLE_TEST)
    add_executable(daily_854_tests tests.cpp)
    target_link_libraries(daily_854_tests PRIVATE project_options catch_main)
    target_link_libraries(daily_854_tests PUBLIC daily_854)

    add_test(NAME Daily854Test COMMAND daily_854_tests)
endif()