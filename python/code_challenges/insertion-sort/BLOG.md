## H0WDY!
<br>
This is my Blog about the amazing algorithm of insertion sort!
<br>
This algorithm does something pretty simple but is wildly important!
<br>
Now it is quite taxing on the computer, with a big O of O(n^2) so try not to scale it up too much!
<br>
First the algorithm takes in an array of integers. [1,4,5,7,45,4]
<br>
Then we do basic outlier checks, like if the array is empty or, if it only has one value. if len(arr) <= 1 throw error!
<br>
Next we make a way to iterate through the array, and in our case we made a for loop that looks like: for i in range(1, len(arr))
<br>
Now that we have iteration, we make a variable called key, that is equal to the iteration index of the array.
<br>
We need another variable to check against so we make one called j, that is equal to the iterated index -1 (so one index behind it in our case, if i was 5, j would be 4)
<br>
Then we set a while loop that fires when j is greater than or equal to 0 and key is less than j. This means if the integer after j is smaller than j, we will continue.
<br>
When our while loop we set j equal to the index in front of it (in our case its key), save that in a variable, then reset it back to one index behind i.
<br>
lastly we set j+1 = arr so wwe can recurse through the array.
<br>
Once all our iterations of the for loop are satisfied, we then return the sorted array!
<br>
Its just that simple, err , not so simple. Either way its a very useful algorithm that can be a handy trick up any programmers sleeve.
