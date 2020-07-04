# Generic test that uses conan libs
add_executable(problem problem.cpp)

target_link_libraries(
  problem
  PRIVATE project_options
)