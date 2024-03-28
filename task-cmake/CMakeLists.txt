
cmake_minimum_required(VERSION 2.6)

project(C)
add_custom_target( 
  GenerateIndex
  DEPENDS A/preparing.py
  BYPRODUCTS A/index.h
  COMMAND python3 ${PROJECT_SOURCE_DIR}/A/preparing.py
)

add_subdirectory(B)
add_subdirectory(C)

