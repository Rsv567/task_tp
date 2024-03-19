#!/usr/bin/env python3

with open("index.h", "w") as f:
    f.write("#ifndef MY_MODULE_H\n")
    f.write("#define MY_MODULE_H\n\n")
    f.write("#include <iostream>\n")
    f.write("void hello_world() {\n")
    f.write("    std::cout<<(\"hello world\");\n")
    f.write("}\n")

    f.write("#endif // MY_MODULE_H\n")
