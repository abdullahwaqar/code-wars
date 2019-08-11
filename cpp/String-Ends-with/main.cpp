/*
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution("abc", "bc"); //returns true
solution("abc", "d"); //returns false
*/

#include <iostream>

bool solution(std::string const &str, std::string const &ending) {
      return str.size() >= ending.size() && str.compare(str.size() - ending.size(), std::string::npos, ending) == 0;
}

int main(int argc, char const *argv[]) {
    solution("abcd", "cd");
    return 0;
}
