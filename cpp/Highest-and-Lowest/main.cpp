/*
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

highAndLow("1 2 3 4 5");  // return "5 1"
highAndLow("1 2 -3 4 5"); // return "5 -3"
highAndLow("1 9 3 4 -5"); // return "9 -5"

Notes:

    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.

*/
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

std::vector<std::string> split(const std::string& str, const char delimeter) {
    std::vector<std::string> internal;
    std::stringstream ss(str);
    std::string tok;

    while(getline(ss, tok, delimeter)) {
        internal.push_back(tok);
    }
    return internal;
}

std::string highAndLowRev1(const std::string& numbers){
    if (!numbers.empty()) {
        std::string retBuffer = "";
        std::vector<std::string> strStream = split(numbers, ' ');
        std::vector<std::string> strStreamCopy = strStream;
        for (std::string it : strStream) {
            for (std::string it1 : strStreamCopy) {
                if (it > it1) {
                    retBuffer += it;
                }
            }
        }
        return retBuffer;
    }
}

std::string highAndLow(const std::string& numbers){
    std::stringstream stream(numbers);

    int a = INT32_MAX, b =INT32_MIN;
    while(!stream.eof()) {
        int number;
        stream>>number;
        if (number>b) b=number;
        if (number<a) a=number;
    }
    std::stringstream res;
    res << b << " "<<a;
    return res.str();
}

int main(int argc, char const *argv[]) {
    // std::string myCSV = "one two three four";
    // std::vector<std::string> sep = split(myCSV, ' ');
    // for(std::string t : sep) {
    //     std::cout << t << "\n";
    // }
    std::cout << highAndLow("1 2 3 4 5");
    return 0;
}
