# Conditional breakpoint allows you to stop execution of your code when some specific condition is met
# addded shortcut for conditional breakpoint vscode : ctr + c + ctr + b
# breakpoints
# conditional breakpoint(Expression)
# Hit count: The 'hit count' controls how many times a breakpoint needs to be hit before it will 'break' execution. Whether a 'hit count' is respected and the exact syntax of the expression vary among debugger extensions.
# Logpoints(log message) : A Logpoint is a variant of a breakpoint that does not "break" into the debugger but instead logs a message to the console.

expense_list = [1203, 2322, 4532, 6432, 6732, 9034, 8426, "9468", 8247]
total_expense = 0
for expense in expense_list:
    total_expense += expense

print("Total expense is:", total_expense)
