<!-- Given an array of integers your solution should find the smallest integer.
For example:

    Given [34, 15, 88, 2] your solution will return 2
    Given [34, -345, -1, 100] your solution will return -345

You can assume, for the purpose of this kata, that the supplied array will not be empty. -->

<?php

    function smallestInteger ($arr) {
        return min($arr);
    }

    print(smallestInteger([3, 5, 10, 1, 4, 55]));
?>