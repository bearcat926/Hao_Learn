/**
 * 数组中唯一只出现一次的数字
 * 在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。
 * 请找出那个只出现一次的数字。
 * 你可以假设满足条件的数字一定存在。
 * 思考题：如果要求只使用 O(n) 的时间和额外 O(1) 的空间，该怎么做呢？
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int findNumberAppearingOnce(vector<int>& nums) {
        int first = 0, second = 0;
        for(auto num : nums){
            first = (first ^ num) & ~second;
            second = (second ^ num) & ~first;
        }
        return first;
    }
};

/**
 * 状态机：
 * 当 (first,second) 为 (0,0) 时, 与一个数进行某种操作 -> 分别与该数二进制的任一位进行操作 
 * 得到结果为：
 * 1.当(first,second)为(0,0)，x = 1时 -> first = 0 ^ 1 & (~0) = 1 & 1 = 1, second = 0 ^ 1 & (~1) = 1 & 0 = 0 -> (first,second) 为 (1,0)
 * 第二次 -> (first,second) 为 (0,1)
 * 第三次 -> (first,second) 为 (0,0)
 * 2.当(first,second)为(0,0)，x = 0时 -> first = 0 ^ 0 & (~0) = 0 & 1 = 0, second = 0 ^ 0 & (~0) = 0 & 0 = 0 -> (first,second) 为 (0,0)
 * 当(first,second)为(1,0)，x = 0时 -> first = 1 ^ 0 & (~0) = 1 & 1 = 1, second = 0 ^ 0 & (~1) = 0 & 0 = 0 -> (first,second) 为 (1,0)
 * 当(first,second)为(0,1)，x = 0时 -> first = 0 ^ 0 & (~1) = 0 & 0 = 0, second = 1 ^ 0 & (~0) = 1 & 1 = 1 -> (first,second) 为 (0,1)
 * 
 * 结论：(first,second) 与 1 进行三次操作则循环，(first,second) 与 0 操作自环
 * 
 * 所以，(first,second)会在与数组中的重复数字进行三次操作后，恢复为(0,0)状态，
 * 而(first,second)会在与数组中的不重复的数字进行操作后，变为(1,0)状态，
 * 则此时first的值就是不重复的数字的值。
 */