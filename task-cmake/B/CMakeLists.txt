cmake_minimum_required(VERSION 2.6)


add_library(lib SHARED lib.cpp lib.h)

target_include_directories(lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../lib)
install(TARGETS lib DESTINATION lib)
