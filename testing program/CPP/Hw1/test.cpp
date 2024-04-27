#include <iostream>
using namespace std;
int main(){
   int count = 0,limit = 10;
    if(count==0 && limit < 20){
        cout<<1;
    }
    if((limit/count)>7||(limit<20))
        cout<<2;
    if((limit<20)||(limit/count)>7)
        cout<<3;
    if((5&&7)+(!6))
        cout<<4;
    return 0;
}