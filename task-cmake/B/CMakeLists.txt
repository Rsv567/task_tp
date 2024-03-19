cmake_minimum_required(VERSION 2.6)


add_library(lib SHARED lib.cpp lib.h)

target_include_directories(lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

