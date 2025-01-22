## Google Online Assessment

### First Question

There is an array, named `digits`, consisting of N digits. Choose at most three digits (not necessarily adjacent) and
merge them into a new integer without changing the order of the digits. What is the biggest number that can be obtained
this way?

Write a function:

def solution(digits)

that, given an array of N digits, returns the biggest number that can be built.

Examples:

Given digits = [7, 2, 3, 3, 4, 9], the function should return 749.
Given digits = [0, 0, 5, 7], the function should return 57.
Assume that:

N is an integer within the range [3..50];
each element of array, named `digits`, is an integer within the range [0..9].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

### Second Question

You begin with an array filled with N zeros and you want to obtain an array A.

In one move, you can choose an arbitrary interval and increase all the elements within that interval by 1. For example,
you can transform [0, 0, 0, 0, 0] into [0, 1, 1, 1, 0] in a single move. However, you need three moves to
obtain [1, 0, 1, 2, 2]. One possible sequence of moves is: [0, 0, 0, 0, 0] → [0, 0, 1, 1, 1] → [0, 0, 1, 2, 2]
→ [1, 0, 1, 2, 2], where → denotes a single move.

What is the minimum number of moves needed to obtain A, starting from a zero-filled array?

Write a function:

int solution(vector<int> &A);

that, given an array A of length N, returns as an integer the minimum number of moves needed to transform a zero-filled
array into A.

Examples:

Given A = [2, 1, 3], the function should return 4. For example, the following sequence of moves leads to the
solution: [0, 0, 0] → [1, 1, 1] → [2, 1, 1] → [2, 1, 2] → [2, 1, 3].
Given A = [2, 2, 0, 0, 1], the function should return 3. The following sequence of moves leads to the
solution: [0, 0, 0, 0, 0] → [1, 1, 0, 0, 0] → [2, 2, 0, 0, 0] → [2, 2, 0, 0, 1].
Given A = [5, 4, 2, 4, 1], the function should return 7. One possible optimal sequence of moves is: [0, 0, 0, 0, 0]
→ [1, 1, 1, 1, 1] → [2, 2, 2, 2, 1] → [3, 3, 2, 2, 1] → [4, 4, 2, 2, 1] → [5, 4, 2, 2, 1] → [5, 4, 2, 3, 1]
→ [5, 4, 2, 4, 1].
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
we guarantee that the answer will not exceed 1,000,000,000.