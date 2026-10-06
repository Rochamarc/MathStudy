#include <iostream>
#include <string>

class Pair{
public:
	int x;
	int y;
	std::string name;

	Pair(int x_value, int y_value){
		x = x_value;
		y = y_value;
	}

	void repr(){
		std::cout << "(" << x << "," << y << ")" << std::endl;
	}
};

int main(void){
	Pair v(2,2);
	Pair u(2,4);

	v.repr();
	v.name = "v";

	u.repr();
	u.name = "u";
	
	return 0;
}