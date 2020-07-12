# Generic test that uses conan libs
add_executable(problem main.cpp problem.h problem.cpp)

target_include_directories(problem PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

target_link_libraries(
  problem
  PRIVATE project_options
)

if( MSVC )
    set_property( DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT problem )
endif()