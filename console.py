#!/usr/bin/python3
"""Command interpreter for HBnB"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBnB"""

    models = ["BaseModel"]
    prompt = '(hbnb) '

    def emptyline(self):
        """Does nothing when it recieves an empty line."""
        pass

    def do_quit(self, *args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program."""
        return True

    def do_create(self, *args):
        """Creates a new instance of an object.
        Usage: create class_name"""
        arg = args[0].split()
        if len(arg) is 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            obj = eval(arg[0]+"()")
            obj.save()
            print(obj.id)

    def do_show(self, *args):
        """Prints the string representation of an instance.
        Usage: show class_name id"""
        arg = args[0].split()
        if len(arg) is 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[key])

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id.
        Usage: destroy class_name id"""
        arg = args[0].split()
        if len(arg) is 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.models:
            print("** class does'n exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in obj_dict:
                print("** no instance found **")
            else:
                del obj_dict[key]
        storage.save()

    def do_all(self, *args):
        """Prints all string representations of all instances\
        based or nor in the class name.
        Usage: all
        Or: all class_name"""
        arg = args[0].split()
        obj_dict = storage.all()
        obj_list = []
        if len(args[0]) == 0:
            for key in obj_dict:
                obj_list.append(obj_dict[key])
            print(obj_list)
        else:
            if arg[0] not in HBNBCommand.models:
                print("** class doesn't exist **")
            else:
                for key, value in obj_dict.items():
                    if (value.to_dict()).get('__class__') == arg[0]:
                        obj_list.append(str(obj_dict[key]))
                print(obj_list)

    def do_update(self, *args):
        """Updates an instance based on the class name and id by\
        adding or updating an attribute.
        Usage: update class_name id attribute_name 'attribute value'
        Only one attribute can be changed or added at a time"""
        arg = args[0].split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in obj_dict:
                print("** no instance found **")
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            obj_keys = obj_dict[key].to_dict()
            if arg[2] in obj_keys:
                value = obj_keys[arg[2]]
                val_type = type(value)
                new_val = eval('val_type'+'('+arg[3]+')')
                setattr(obj_dict[key], arg[2], new_val)
            else:
                setattr(obj_dict[key], arg[2], arg[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
