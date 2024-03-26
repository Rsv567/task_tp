import os


current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, 'index.h')

with open(file_path, "w") as f:
    f.write("#ifndef MY_MODULE_H\n")
    f.write("#define MY_MODULE_H\n\n")
    f.write("#include <iostream>\n")
    f.write("void hello_world() {\n")
    f.write("    std::cout<<(\"hello world\");\n")
    f.write("}\n")

    f.write("#endif // MY_MODULE_H\n")
print("dffhrhhg")
