add_library(catch_main STATIC catch_main.cpp)
target_link_libraries(catch_main PUBLIC Catch)
target_link_libraries(catch_main PRIVATE project_options)

add_executable(tests tests.cpp)
target_link_libraries(tests PRIVATE project_options catch_main)

add_test(NAME MyAwesomeTest COMMAND tests)