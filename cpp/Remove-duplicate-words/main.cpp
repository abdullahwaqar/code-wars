/*
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'
*/

#include <iostream>
#include <string>
#include <map>


std::string removeDuplicateWords(const std::string& str) {
    std::string result, word;
    std::map<std::string, bool> words;
    auto out = [&]() {
        if ((word.size() > 0) && (!words[word])) {
            result.append(((result.size() > 0) ? " " : "") + word);
        }
    };
    for (auto c : str) {
        if (c == ' ') {
            out();
            words[word] = true;
            word = "";
        } else {
             word.push_back(c);
        }
    }
    out();
    return std::move(result);
}

int main(int argc, char const *argv[]) {
    std::cout << removeDuplicateWords("alpha beta beta gamma gamma gamma delta");
    return 0;
}
