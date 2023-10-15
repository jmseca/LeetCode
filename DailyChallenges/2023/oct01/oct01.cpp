#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        int size = s.size();
        string returnStr, myStack;
        returnStr.reserve(size);
        myStack.reserve(size);

        for (int i = 0; i < size; i++){
            if (s[i] == ' '){
                for (int it = (myStack.size() - 1); it >= 0; --it) {
                    returnStr+=myStack[it];
                }
                returnStr+=s[i];
                myStack.clear();
            } else {
                myStack+=s[i];
            }
            
        }
        for (int it = (myStack.size() - 1); it >= 0; --it) {
            returnStr+=myStack[it];
        }
        return returnStr;
    }
};


int main(){

    Solution solution;

    // Call the reverseWords method on the instance
    string input = "Hello World";
    string result = solution.reverseWords(input);

    // Display the result
    cout << "Original string: " << input << endl;
    cout << "Reversed string: " << result << endl;
    
    return 0;
}