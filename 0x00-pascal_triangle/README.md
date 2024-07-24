##0x00. Pascal's Triangle

Pascals triangle or Pascal's triangle is an arrangement of binomial coefficients in triangular form. It is named after the French mathematician Blaise Pascal. The numbers in Pascal's triangle are placed in such a way that each number is the sum of two numbers just above the number. Pascals triangle is used widely in probability theory, combinatorics, and algebra.

Generally, we can use Pascal's triangle to find the coefficients of binomial expansion, to find the probability of heads and tails in a toss, in combinations of certain things, etc. Let us discuss Pascals triangle in detail in the following section.

##Tasks
0. Pascal's Triangle

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
Repo:

GitHub repository: alx-interview
Directory: 0x00-pascal_triangle
File: 0-pascal_triangle.py
