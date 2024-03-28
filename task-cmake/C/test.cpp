#include "../A/index.h"
#include "../B/lib.h"
#include <gtest/gtest.h>
TEST(MYTEST, Test1){
  ASSERT_EQ(12345, hello_world());
}
TEST(MYTEST, TEST2){
  ASSERT_EQ(5, function(2,3));
}
