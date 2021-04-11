# Generic test that uses conan libs
add_library(daily_18 OBJECT findmaxofK.cpp)

target_include_directories(daily_18 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

target_link_libraries(
    daily_18
  PRIVATE project_options
)

if( MSVC )
    set_property( DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT daily_18 )
endif()

##### TESTS
message("This is " ${ENABLE_TEST})
if (ENABLE_TEST)
    add_executable(daily_18_tests tests.cpp)
    target_link_libraries(daily_18_tests PRIVATE project_options catch_main)
    target_link_libraries(daily_18_tests PUBLIC daily_18)

    add_test(NAME Daily18Test COMMAND daily_18_tests)
endif()