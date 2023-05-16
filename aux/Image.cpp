#include "Image.hpp"

namespace prog
{
  Image::Image(int w, int h, const Color &fill = {255, 255, 255}){
    w_=w;
    h_=h;
    array.resize(w, std::vector<Color>(h));
    for(int i=0;i<int(w_);i++){
      for(int j=0;j<int(h_);j++){
        array[i][j]=fill;
      }
    }
  }
  Image::~Image(){}
  int Image::width() const
  {
    return w_;
  }
  int Image::height() const
  {
    return h_;
  }
  Color& Image::at(int x, int y)
  {
    return array[x][y];
  }
  const Color& Image::at(int x, int y) const
  {
    return array[x][y];
  }
  void Image:: invert(){
    for(int i=0;i<int(w_);i++){
      for(int j=0;j<int(h_);j++){
        array[i][j]=Color(255-array[i][j].red(), 255-array[i][j].green() , 255-array[i][j].blue());
      }
    }
  }
  void Image::to_gray_scale(){
    for(int i=0;i<int(w_);i++){
      for(int j=0;j<int(h_);j++){
        rgb_value v =int((array[i][j].red()+array[i][j].green()+array[i][j].blue())/3);
        array[i][j]=Color(v,v,v);
      }
    }
  }
  void Image::replace(rgb_value red1,rgb_value green1,rgb_value blue1,rgb_value red2,rgb_value green2,rgb_value blue2){
    for(int i=0;i<int(w_);i++){
      for(int j=0;j<int(h_);j++){
        if(array[i][j].red()==red1&&array[i][j].green()==green1&&array[i][j].blue()==blue1){
          array[i][j]=Color(red2, green2 , blue2);
        }
      }
    }
  }
   void Image::h_mirror(){
    int k=1; //Será 0 ou 1?
    for(int i=w_/2;i<=w_;i++){
      for(int j=0;j<=h_;j++){
          array[i][j]=array[i-k][j];
        }
      }
      k++;
      k++;
    }

}