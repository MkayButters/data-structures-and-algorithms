## Quick Sort Explained

1. Picks the last position of the list as pivot.

2. Then compares the first element of the list. If this first element is less than the pivot, we go to the next number in the list.

3. This goes until it comes into contact with a number greater than the pivot and it swaps the pivot with the greater number element.

4. Then we go to the opposite side, comparing from the end of the list. If the element is greater than pivot we -1 down the list. If it is less than we swap the elements place with pivots place.

5. This will recurse until the pivot moves no longer.

6. Then the 2 sides of the pivot are split up and 1-5 is repeated with each of the sub-lists

7. We stop this recursion until the sub array contains only one element and the list is sorted.
