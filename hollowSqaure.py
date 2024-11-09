'''Hollow Square of side 'N'
Problem Description:

You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).



Input Parameters:

n (int): The size of the square (number of rows and columns).



Output:

A list of strings where each string is a row of n characters, representing a hollow square.



Example:

Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']


Disclaimer: This Udemy coding exercise is still in development, so some advanced complexities might not be fully checked. Please use it primarily for basic code validation.
'''


Solution ->

def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    
    if n == 1:
        
        return ['*']
    
    final_list = []
    
    final_list.append('*'*n)
    
    for i in range(n-2):
        final_list.append('*'+' '*(n-2) + '*')
        
    final_list.append('*'*n)
    
    return final_list
