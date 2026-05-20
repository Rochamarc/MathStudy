#include <iostream>
#include <string>

std::string bool_in_string(bool val){
	if(val){
		return "True";
	}
	return "False";
}

std::string denial(bool p){
	return bool_in_string(not p);
}

std::string conjuction(bool p, bool q){
	return bool_in_string(p and q);
}

std::string disjunction(bool p, bool q){
	return bool_in_string(p or q);
}

std::string conditional(bool p, bool q){
	if(p and not q){
		return bool_in_string(false);
	}
	return bool_in_string(true);
}

std::string biconditional(bool p, bool q){
	if(p == q){
		return bool_in_string(true);
	}
	return bool_in_string(false);
}


int main(void){
	std::cout << "The denial of true is: " << denial(true) << std::endl;
	std::cout << "The conjuction between true and false is: " << conjuction(true, false) << std::endl;
	std::cout << "The disjunction between true and false is: " << disjunction(true, false) << std::endl;

	std::cout << "The conditional of true and false is: " << conditional(true, false) << std::endl;
	std::cout << "The conditional of false and true is: " << conditional(false, true) << std::endl;
	
	std::cout << "The biconditional of false and true is: " << biconditional(false, true) << std::endl;
	std::cout << "The biconditional of false and false is: " << biconditional(false, false) << std::endl;
	std::cout << "The biconditional of true and true is: " << biconditional(true, true) << std::endl;


	return 0;
}