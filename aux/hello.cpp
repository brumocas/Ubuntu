// example.hpp
#ifndef EXAMPLE_HPP
#define EXAMPLE_HPP

class Example {
public:
  void sayHello();
};

#endif


// example.cpp
#include "example.hpp"
#include <iostream>

void Example::sayHello() {
  std::cout << "Hello from Example!" << std::endl;
}


// main.cpp
#include "example.hpp"

int main() {
  Example example;
  example.sayHello();
  return 0;
}
