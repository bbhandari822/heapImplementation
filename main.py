# Binod Bhandari
# Drexel University 2017
# CS 260-002Summer 2017
# Assignment 5: main.py

from heap import *
import sys

def sort():
    new_list = []
    heap_local = heap
    while (len(heap_local.__str__()) != 0):
        minimum = heap_local.min()
        new_list.append(minimum)
        heap_local.deletemin()
    print("\n".join(str(e) for e in new_list))

def help():
    print ("help - Prints this list \n"
           "makenull - Clears the heap \n"
           "insert <integer> - Inserts the number into the heap\n"
           "min - Prints the current min on the heap \n"
           "inorder - Prints heap in inorder\n"
           "preorder - Prints heap in preorder \n"
           "postorder - Prints heap in postorder \n"
           "deletemin - Removes min from the heap \n"
           "sort - Calls deletemin repeatedly to print out sorted numbers \n"
           "exit - Exits the program (also Crtl-D exits) ")
if __name__ == '__main__':

    heap = heap()
    print("Welcome to the Heap")
    print("The List of Commands is below, type help to see them again.")
    print("help - Prints this list")
    print("makenull - Clears the heap")
    print("insert <integer> - Inserts the number into the heap")
    print("min - Prints the current min on the heap")
    print("inorder - Prints heap in inorder \n"
          "preorder - Prints heap in preorder\n"
          "postorder - Prints heap in postorder\n"
          "deletemin - Removes min from the heap\n"
          "sort - Calls deletemin repeatedly to print out sorted numbers\n"
          "exit - Exits the program (also Crtl-D exits)")

    while True:  # check until the exit or Ctrl+D is entered
        try:
            command = input(">")
        except (EOFError):
            break
        if len(command) == 0:
            print("Bad Command - type help for commands")

        elif ((command.split())[0]) == "exit":
            sys.exit (0)

        elif ((command.split())[0]) == "help":
            help()

        elif ((command.split())[0]) == "":
            print("Please enter the following command")

        elif ((command.split())[0]) == "makenull":
            heap.makenull()

        elif ((command.split())[0]) == "insert":
            if len(command.split()) != 2:
                print("Insert number, cannot take empty value")
            else:
                a = int((command.split())[1])
                heap.insert(a)

        elif ((command.split())[0]) == "min":
            print(heap.min())

        elif ((command.split())[0]) == "deletemin":
            heap.deletemin()

        elif ((command.split())[0]) == "inorder":
            print(heap.inorder(0))

        elif ((command.split())[0]) == "preorder":
            print(heap.preorder(0))

        elif ((command.split())[0]) == "postorder":
            print(heap.postorder(0))

        elif ((command.split())[0]) == "sort":
            sort()

        elif ((command.split())[0]) != "help" or "makenull" or "insert" or "min" or "inorder" or \
                "preorder" or "postorder" or "deletemin" or "sort" or "exit":
            print("Bad Command - type help for commands")