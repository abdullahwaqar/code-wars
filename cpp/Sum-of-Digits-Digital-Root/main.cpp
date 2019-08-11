/*
n this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
*/

#include <iostream>

int getSum(int n) {
    int num = n;
    int s = 0;
    while (num != 0) {
        s = s + num % 10;
        num = num / 10;
    }
    return s;
}

int digital_root(int n) {
    int length = std::to_string(n).length();
    int tempHolder = n;
    while (length != 1) {
        tempHolder = getSum(tempHolder);
        length = std::to_string(tempHolder).length();
    }
    return tempHolder;
}

// Not my solutions but the are wicked
int _digital_root(int n)
{
  return (n-1) % 9 +1;
}

int digital_root_(int Z) {
    return --Z % 9 + 1;
}

int main(int argc, char const *argv[]) {
    std::cout << digital_root(493193) << '\n';
    std::cout << digital_root(132189) << '\n';
    return 0;
}
