#!/usr/bin/python3
"""Command interpreter for HBnB"""
import cmd
from models import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBnB"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Does nothing when it recieves an empty line"""
        pass

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program"""
        return True

    def create(self, *args):
        """Creates a new instance of an object
        Usage: create class_name"""
        models = ["BaseModel"]
        if len(args) is 0:
            print("** class name missing **")
        elif args is not in models:
            print("** class doesn't exist **")
        else:
            obj = eval(arg+"()")
            print(obj.id)
            obj.save()

    def show(self, *args):
        """Prints the string representation of an instance
        Usage: show class_name id
        """


if __name__ == "__main__":
    HBNBCommand().cmdloop()
