#!/usr/bin/python3
"""This is the `console` module

It constains the entry point of the command interpreter
"""

from models import storage
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This has methods used for the command interpreter for the console"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review,
    }

    def emptyline(self):
        """Method to override the pre-existing `emptyline()`"""

        pass

    def help_quit(self):
        """Documentation for the quit command"""

        print("Quit the command interpreter")

    def do_EOF(self, arg):
        """Exit the program by typing on EOF"""

        print()
        return True

    def do_quit(self, arg):
        """Exit the program by typing `quit`"""

        return True

    def do_create(self, arg):
        """Creates a new instance of a class

        Example:
            (hbnb) create BaseModel
            <BaseModel.id>
        """

        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class name missing **")
        else:
            new_model = HBNBCommand.__classes[arg]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class & id

        Example:
            (hbnb) show BaseModel 1234-1234-1234
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                obj_dict = storage.all()
                obj_key = "{}.{}".format(args[0], args[1])
                print(obj_dict[obj_key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                obj_dict = storage.all()
                obj_key = "{}.{}".format(args[0], args[1])
                del obj_dict[obj_key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances

        They can be based or not on the class name
        """

        args = arg.split()
        if len(args) == 0:
            print([str(val) for val in storage.all().values()])
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print([str(val) for val in storage.all().values()
                  if type(val).__name__ == args[0]])

    def do_update(self, arg):
        """Updates the attribute of a given instance

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_id = args[1]
        try:
            obj_dict = storage.all()
            obj_key = "{}.{}".format(class_name, obj_id)
            obj = obj_dict[obj_key]
        except KeyError:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if attr_name in ["id", "created_at", "updated_at"]:
            print("** cannot update this attribute **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        attr_value = args[3].strip('"')
        try:
            attr_value = int(attr_value)
        except ValueError:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
