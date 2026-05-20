#include <iostream>
#include <string>
#include <cmath>


class Exponential{
public:
	int a;
	
	Exponential(int base){
		a = base;
	}
	

	void name() {
		std::cout << "f(x)=" << a << "^x" << std::endl;
	}

	int calculate(float x){
		return std::pow(a, x);
	}

	void simple_table(){
		// just a simple method to calculate x equal to 0,1,2 and 3.
		for(int i = 0; i <= 3; i++){
			std::cout << a << "^" << i << "=" << calculate(i) << std::endl;
		}
	}
};


int main(void){
	Exponential exp(2);

	exp.name(); // pego a lei de formação

	// calculando para x = 2
	// std::cout << e.calculate(2) << std::endl;
	exp.simple_table();
	
	return 0;
}