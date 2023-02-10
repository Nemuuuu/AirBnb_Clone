#!/usr/bin/python3

import cmd
import models
from shlex import split as split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

new_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'Amenity': Amenity, 'Place': Place, 'City': City,
               'Review': Review}

# Declare the HBNBCommand class
class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = '(hbnb)$ '

    def do_help(self, args):
        if args == "quit" or args == "EOF":
            print("Quit command to exit the program\n")
        elif args == "create":
            print("Create command to create new User\n")
        elif args == "show":
            print("Show command to show an instance based on class name and id\n")
        elif args == "destroy":
            print("Delete command to delete an instance based on class name and id\n")
        elif args == "all":
            print("All command to print all instances based or not class name\n")
        elif args == "update":
            print("Update command to update an instance base on class name and id by adding or updating attribute\n")
        else:
            print("\nDocumented commands (type help <topic>):")
            print("=================================")
            print("EOF\tall\tcreate\tdestroy\thelp\tquit\tshow\tupdate")
# quit and EOF to exit the program

    def do_EOF(self, line):
        """

        """
        return true

    def do_quit(self, line):
        """

        """
        return True
    def emptyline(self):
        """
        """
        pass

    def ENTER(self):
        """
        """
        pass

    def do_create(self, line):
        """

        """
# If the class name is missing, print ** class name missing ** (ex: $ create)
# If the class name doesn’t exist, print ** class doesn't exist **
# (ex: $ create MyModel)
        splitline = split(line)
        if not splitline:
            print("** class name missing **")
        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")
        else:
            new_instance = new_classes[splitline[0]]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """

        """
        splitline = split(line)

# If the class name is missing, print ** class name missing **
# (ex: $ show)

        if not splitline:
            print("** class name missing **")
# If the class name doesn’t exist, print ** class doesn't exist **
# (ex: $ show MyModel)

        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")

# If the id is missing, print ** instance id missing **
# (ex: $ show BaseModel)

        elif len(splitline) < 2:
            print("** instance id missing **")

# If the instance of the class name doesn’t exist for the id,
# print ** no instance found ** (ex: $ show BaseModel 121212)
        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[new_instance])

    def do_destroy(self, line):
        """
        """
        splitline = split(line)

#If the class name is missing,
# print ** class name missing **
#(ex: $ destroy)

        if not splitline:
            print("** class name missing **")
            return False
# If the class name doesn’t exist,
# print ** class doesn't exist **
# (ex:$ destroy MyModel)

        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")

# If the id is missing,
# print ** instance id missing **
# (ex: $ destroy BaseModel)

        elif len(splitline) < 2:
            print("** instance id missing **")

# If the instance of the class name
# doesn’t exist for the id
# print ** no instance found **
# (ex: $ destroy BaseModel 121212)
        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[new_instance]
                models.storage.save()

    def do_all(self, line):
        """
        """
        str_list = []
# If the class name doesn’t exist,
# print ** class doesn't exist **
# (ex: $ all MyModel)
        if not line:
            for new_instance in models.storage.all().values():
                str_list.append(str(new_instance))
        else:
            splitline = split(line)
            if splitline[0] in new_classes:
                for key, value in models.storage.all().items():
                    if value.__class__.__name__ == splitline[0]:
                        str_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return False
        print(str_list)
# The printed result must be a list of strings

    def do_update(self, line):
        """
        """
        splitline = split(line)

#print ** class name missing ** (ex: $ update)
#
        if not splitline:
            print("** class name missing **")

# If the class name doesn’t exist,
# print ** class doesn't exist **
#(ex: $ update)

        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")

# If the id is missing,
#print ** instance id missing **
#(ex: $ update BaseModel)

        elif len(splitline) < 2:
            print("** instance id missing **")

#print ** attribute name missing **
#(ex: $ update BaseModel existing-id)
#

        elif len(splitline) < 3:
            print("** attribute name missing **")
#print ** value missing **
#(ex: $ update BaseModel existing-id first_name)
#

        elif len(splitline) < 4:
            print("** value missing **")

#If the instance of the class name doesn’t exist for the id,
#print ** no instance found **
#(ex: $ update BaseModel 121212)
        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[new_instance],
                        splitline[2], splitline[3])
                models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
