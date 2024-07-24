# 5. Pattern Printing: Write a Python program to print the following pattern using nested loops:
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *

rows_number = 5

for i in range(1, rows_number+1):
    for j in range(1, i+1):
        print("*", end=' ')
    print()
    
    
# khali print next line dega kuki by default jo end hota h wo /n hota h. or isliye ooper wale ko same line me print karane k lye humne end ko space se lya hai.