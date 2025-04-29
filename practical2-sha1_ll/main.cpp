#include <iostream>
#include "sha256.h"

int main()
{
    std::string key = "hello";
    std::string hashValue = sha256(key);
    std::cout << "SHA-256 hash for '" << key << "' is: " << hashValue << std::endl;
    return 0;
}