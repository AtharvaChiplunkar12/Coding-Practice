package matrix;

/*
861. Score After Flipping Matrix
Type - Medium

Topics - Array, Greedy, Bit Manipulation, Matrix

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

 

Example 1:

Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:

Input: grid = [[0]]
Output: 1

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 20
    grid[i][j] is either 0 or 1.
*/

class Solution {
    public int matrixScore(int[][] grid) {
        int[] colCount = new int[grid[0].length];
        for(int i = 0; i < grid.length; i++){
            if(grid[i][0] == 0){
                for(int j = 0; j < grid[i].length; j++){
                    if(grid[i][j] == 0){
                        grid[i][j] = 1;
                    }else{
                        grid[i][j] = 0;
                    }
                }
            }
            for(int j = 0; j < grid[i].length; j++){
                if(grid[i][j] == 0){
                        colCount[j]--;
                    }else{
                        colCount[j]++;
                    }       
            }
        }
        for(int i = 0; i < grid[0].length; i++){
            if(colCount[i] < 0){
                for(int j = 0; j < grid.length; j++){
                    if(grid[j][i] == 0){
                        grid[j][i] = 1;
                    }else{
                        grid[j][i] = 0;
                    }
                }
            }
        }

        int out = 0;
        for(int i = 0; i < grid.length; i++){
            int decimal = 0;
            for(int j = 0; j < grid[i].length; j++){
                //System.out.print(grid[i][j]);
                decimal = decimal*2 +  grid[i][j];
            }
            //System.out.println();
            out+=decimal;
        }

        return out;
    }
}