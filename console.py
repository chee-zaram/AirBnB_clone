#!/usr/bin/python3
"""This is the `console` module

It constains the entry point of the command interpreter
"""

from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """This has methods used for the command interpreter for the console"""

    prompt = "(hbnb) "
    __classes = storage.classes

    def emptyline(self):
        """Method to override the pre-existing `emptyline()`"""
        pass

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
        """Prints the string representation of all instances

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

        # TODO: use regex to extract what is in the double quotes to preserve
        # multi-word strings

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

    def help_EOF(self):
        """Prints help for the EOF command"""

        print("Exits the program when it receives and EOF signal\n")

    def help_quit(self):
        """Documentation for the quit command"""

        print("Quit the command interpreter\n")

    def help_create(self):
        """Prints the help for `create` command"""

        print("Creates a new instance of a class")
        print("Example:\n  (hbnb) create BaseModel <BaseModel.id>\n")

    def help_show(self):
        """Prints help for `show` command"""

        print("Prints the string representation of an instance based on class",
              end='')
        print(" and id\nExample:\n  (hbnb) show BaseModel 1234-1234-1234\n")

    def help_destroy(self):
        """Prints help for `destroy` command"""

        print("Deletes an instance based on class name and id")
        print("Example:\n  (hbnb) destroy BaseModel 1234-5678-1234\n")

    def help_all(self):
        """Prints help for `all` command"""

        print("Displays the string representation of all instances")
        print("Example:\n  (hbnb) all\n")
        print("They can also be printed based on class name")
        print("Example:\n  (hbnb) all User\n")

    def help_update(self):
        """Prints the help for `update` command"""

        print("Update the value for a given attribute\nUsage: ", end="")
        print('update <class name> <id> <attribute name> "<attribute value>"')
        print('Example:\n  (hbnb) update City 1234-5678 name "New York"\n')


if __name__ == "__main__":
    HBNBCommand().cmdloop()
