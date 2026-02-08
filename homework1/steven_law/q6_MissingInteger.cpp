/*Time Complexity: O(log n)
Space Complexity: O(1)
Technique used: Binary Search
Time Taken: 19mina 41secomds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

int missingInteger(vector<int>& nums){
    int l = 0;
    int r = nums.size() - 1;
    int lastMid = 0;

    while(l<=r){
        int mid = l+ (r-l) / 2;

        if(nums[mid] - mid == 1) l = mid + 1;
        else r = mid - 1;

        lastMid = mid;
    }
    return nums[lastMid] + 1;
}


int main(){
    vector<int> arr1 = {1, 2, 3, 4, 6, 7};
    int n1 = 7;
    cout << "Expected: 5" << endl;
    cout << "Output:   " << missingInteger(arr1) << endl << endl;

    vector<int> arr2 = {1};
    int n2 = 2;
    cout << "Expected: 2" << endl;
    cout << "Output:   " << missingInteger(arr2) << endl << endl;

    vector<int> arr3 = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12};
    int n3 = 12;
    cout << "Expected: 9" << endl;
    cout << "Output:   " << missingInteger(arr3) << endl;

    return 0;
}

/* psudocode/thoughts/logic
goal: Find the missing integer in an array
restraints: none
strategy:
I was thinking a two pointer approach where the right is 1 index faster
than the left and if the value of right - left is more than 1 , we found
our number. this is a very intuative approach and is very straight forward
so I think we can do better. looking at the problem we know the array is
sorted and we know the size of the array or how many elements are in it.
With that being said , in an array we know the values are 0 indexed 
so for example:

{1, 2, 3, 4, 6, 7}
0:1 , 1:2, 2:3, 3:4, 4:6, 5:7

We can cleary see a pattern. before the missing value or 5 all the values
have a corisponding index of their own minus 1 so for instance, at index
0 we have value 1 or at value 1 we have index 0, there is a difference of
1 here, same thing with 2, and 3 and 4. when we get to 6 the index is 4 
which is a difference of 2. so we know value 4 has index 3 and 
value 6 has index 4. knowing this all we have to do now is cut the 
array in half and check if the index makes sense or not. if it does
delete the left side andfocus on the new set because our missing value
has to be in there. with this new set do the same thing cut in half, and
identify if the index makes sense. continue this process till you cant
and the last value to make sense or what you end up on should direct u 
to the missing value if you add one so for instance:

0:1 , 1:2, 2:3, 3:4, 4:6, 5:7
size: 6

now the midde is index 2 or value 3 since we floor it.
we check if value - index = 1. it is. delete the left side or just ignore 
it. now we have:

 3:4, 4:6, 5:7
 size: 3

 floor division we get index 3 value 4 which is 4-3 = 1 
 its valid so remove and focus on 

 4:6, 5:7
 size: 2

we check 6-2 = 2...not valid it does not = 1. delete the right side
we end up with 4:6 so we know the value we are looking for is 6-1 = 5.

im going to try this again with another set just to be sure:

pass 1:
{1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12}

mid = 6 index 5
6 - 5 = 1
cut left 

{7, 8, 10, 11, 12}

mid = 8 index 7
8-7 = 1
cut left

{10, 11, 12}

mid = 10 index 8 
10 - 8 = 2
invalid.
missing value is 10-1= 9. looks good.

*/