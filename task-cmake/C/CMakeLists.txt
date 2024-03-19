cmake_minimum_required(VERSION 2.6)
add_executable(main main.cpp)
target_link_libraries(main lib)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)

install(TARGETS main DESTINATION bin) 
