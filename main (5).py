Challenge3.1

#include <iostream>

#include <vector>

#include <string>

std::vector<int> linear_search_product(const

std::vector<std::string>& product_list

std::string& target_product) {

std::vector<int> indices;

for (int i = 0; i < product_list.size(); ++i) { if (product_list[i] == target_product) { indices.push_back(); }

}int main() {

X

std::vector<std::string> products = {"apple", "banana", "apple", "orange", "apple"); std::vector<int> result = linear_search_product(products, target);

std::string target = "apple":

if (result.empty()) { std::cout << "Product not found." <<

std::endl;

} else {

std::cout << "Product found at indices: "; for (int index: result) {

std::cout << index <<"";

}

std::cout << std::endl;

}

return 0;