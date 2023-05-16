#ifndef prog_Image_hpp
#define prog_Image_hpp
#include "Color.hpp"
#include<iostream>
#include<vector>

namespace prog
{
  class Image
  {
  private:
    int w_;
    int h_;
    std::vector<std::vector<Color>> array;
  public:
    Image(int w, int h, const Color &fill = {255, 255, 255});
    ~Image();
    int width() const;
    int height() const;
    Color &at(int x, int y);
    const Color &at(int x, int y) const;
    void invert();
    void to_gray_scale();
    void replace(rgb_value red1,rgb_value green1,rgb_value blue1,rgb_value red2,rgb_value green2,rgb_value blue2);
    void h_mirror();
  };
}
#endif