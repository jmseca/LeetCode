#include <iostream>
#include <string>
#include <algorithm>
#include <stdio.h>

using namespace std;

class Solution {
public:
    bool winnerOfGame(string colors) {
        int streak = 0, alicePlays = 0, bobPlays = 0, size_1 = colors.size() - 1;
        bool aStreak = false;
        char chr;
        for (int i = 0; i<=(size_1); i++){
            chr = colors[i];
            if (chr == 'A'){
                if (aStreak){
                    streak += 1;
                } else {
                    bobPlays += max(0,streak-2);
                    aStreak = true;
                    streak = 1;
                }
            } else {
                if (aStreak){
                    alicePlays += max(0,streak-2);
                    aStreak = false;
                    streak = 1;
                } else {
                    streak+=1;
                }
            }
        }
        if (streak >= 3){
            if (aStreak){
                alicePlays += max(0,streak-2);
            } else {
                bobPlays += max(0,streak-2);
            }
        }
        return alicePlays && alicePlays > bobPlays;
    }
};


int main(){

    Solution solution;

    string input = "BBBAAAABB";

    cout << "Input = " << input << endl << solution.winnerOfGame(input) << endl;

    return 0;
}