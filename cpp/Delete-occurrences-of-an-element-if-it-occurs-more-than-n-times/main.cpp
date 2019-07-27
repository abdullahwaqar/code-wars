/*
Enough is enough!

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like this sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?
Task

Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
Example

  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
*/

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>

std::vector<int> deleteNthRev1(std::vector<int> arr, int n) {
    std::vector<int> sorted = {};
    std::map<int, int> store;
    //* Loop to set inatial map
    for (auto it = arr.begin(); it != arr.end(); it++) {
        if (!store[*it]) {
            store[*it] = 0;
        }
        for (auto storeIt = store.begin(); storeIt != store.end(); storeIt++) {
            if (storeIt->first == *it) {
                storeIt->second += 1;
            }
        }
    }
    for (auto storeIt = store.begin(); storeIt != store.end(); storeIt++) {
        if (storeIt->second <= n) {
            sorted.push_back(storeIt->first);
        }
        std::cout << storeIt->first << ':' << storeIt->second << '\n';
    }
    return sorted;
}

std::vector<int> deleteNth(const std::vector<int>& xs, int n) {
    std::vector<int> res;
    std::unordered_map<int, int> ns;
    for (int x : xs) {
        if (ns[x]++ < n)
            res.push_back(x);
    }
  return res;
}

int main(int argc, char const *argv[]) {
    deleteNth({1, 2, 3, 2, 2, 2}, 2);
    return 0;
}
