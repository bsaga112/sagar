# Data inspection
# Variables can be inspected in the VARIABLES section of the Run view or by hovering over their source in the editor
# Variables and expressions can also be evaluated and watched in the Run view's WATCH section.
# By using the Call Stack window, you can view the function or procedure calls that are currently on the stack. The Call Stack window shows the order in which methods and functions are getting called. The call stack is a good way to examine and understand the execution flow of an app.
def foo():
    bar()


def bar():
    pass


foo()

# TODO: https://www.sqlshack.com/how-to-debug-python-scripts-in-visual-studio-code/

# Variables Pane – Using the variables pane you can easily inspect the data elements within your program. When you start debugging a lot of system-defined variables are initiated along with the user-defined variables. During the debugging session, you can verify the values of each of those variables from this pane.

# Watch Pane – Sometimes you may write a program with hundreds of variables within it. It is not possible to monitor the values of all those variables from the Variables pane as mentioned above. In such a case, you might want to monitor only one or two variables of your choice leaving the worry about the rest. You can add those variables to your watch list, and you can easily monitor the status and the values for those particular variables within this pane.

# Call Stack(Frames) Pane – This is helpful when your code has a lot of inner methods and you navigate deep inside a stack and then you might lose track of your stack. When there is any error in your program you can easily know from which stack is the error has occurred and then debug it accordingly.
