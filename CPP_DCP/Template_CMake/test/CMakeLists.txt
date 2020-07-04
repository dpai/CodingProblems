add_library(catch_main STATIC catch_main.cpp)
target_link_libraries(catch_main PUBLIC Catch)
target_link_libraries(catch_main PRIVATE project_options)

add_executable(tests tests.cpp )
target_link_libraries(tests PRIVATE project_options catch_main)

## If using problem_tests as OBJECT, uncomment below 3 lines
#add_library(problem_tests OBJECT ${CMAKE_SOURCE_DIR}/src/problem.h ${CMAKE_SOURCE_DIR}/src/problem.cpp )
#target_include_directories(tests PUBLIC ${CMAKE_SOURCE_DIR}/src)
#target_link_libraries(tests PUBLIC $<TARGET_OBJECTS:problem_tests>)

## If using problem_tests as STATIC, uncomment below 3 line
add_library(problem_tests STATIC ${CMAKE_SOURCE_DIR}/src/problem.h ${CMAKE_SOURCE_DIR}/src/problem.cpp)
target_include_directories(problem_tests INTERFACE ${CMAKE_SOURCE_DIR}/src)
target_link_libraries(tests PUBLIC problem_tests)

add_test(NAME MyAwesomeTest COMMAND tests)