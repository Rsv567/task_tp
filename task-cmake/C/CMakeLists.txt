cmake_minimum_required(VERSION 2.6)



add_executable(C main.cpp)
add_dependencies(C GenerateIndex)

target_include_directories(C PUBLIC  ${PROJECT_SOURCE_DIR})


target_link_libraries(C lib)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/../bin)


install(TARGETS C DESTINATION bin) 




include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/5376968f6948923e2411081fd9372e71a59d8e77.zip
)
FetchContent_MakeAvailable(googletest)
enable_testing()
add_executable(Tests main_test.cpp test.cpp)
target_link_libraries(Tests GTest::gtest_main lib)
include(GoogleTest)
gtest_discover_tests(Tests)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/../bin)


install(TARGETS Tests DESTINATION bin) 
set_target_properties(Tests PROPERTIES OUTPUT_NAME CTest)


