/**
 * 数的三次方根
 * 给定一个浮点数n，求它的三次方根。
 * 
 * 输入格式
 * 共一行，包含一个浮点数n。
 * 
 * 输出格式
 * 共一行，包含一个浮点数，表示问题的解。
 * 注意，结果保留6位小数。
 * 
 * 数据范围
 * −10000 ≤ n ≤ 10000
 * 
 * 输入样例：
 * 1000.00
 * 
 * 输出样例：
 * 10.000000
 */

#include<iostream>
using namespace std;

int main(){
    
    double x;
    cin >> x;
    
	// 如果是负数，则要转正数
    double t = x > 0 ? x : -x;
    double l = 0, r = t;
    
	// 精度为6位小数，但要扩大两位保证精度
    while(r - l > 1e-8){
        double mid = (l + r) / 2;
        // 3次方大于x，则在左侧
        if(mid * mid * mid >= t) r = mid;
        else l = mid;
    }
    printf("%lf\n", x > 0 ? l : -l);
    return 0;
}