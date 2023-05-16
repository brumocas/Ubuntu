#ifndef prog_Script_hpp
#define prog_Script_hpp

#include <string>
#include <fstream>
#include "Image.hpp"

namespace prog
{
  class Script
  {
  public: 
    Script(const std::string &filename);
    ~Script();
    void run();
    void invert();
    void to_gray_scale();
    void replace(rgb_value red1,rgb_value green1,rgb_value blue1,rgb_value red2,rgb_value green2,rgb_value blue2);
  private:
    // Current image.
    Image *image;
    // Input stream for reading script commands.
    std::ifstream input;

  private:
    // Private functions
    void clear_image_if_any();
    void open();
    void blank();
    void save();

  };
}
#endif