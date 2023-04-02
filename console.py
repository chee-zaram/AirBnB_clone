#!/usr/bin/python3
"""This is the `console` module

It contains the entry point of the command interpreter
"""

from models import storage, storage_type
from models.engine.file_storage import FileStorage
import cmd
import re
import json


class HBNBCommand(cmd.Cmd):
    """This is the `hbnb` command interpreter which inherits from `cmd.Cmd`

    It serves the purpose of managing the classes and objects used within the
    `AirBnB_clone` project.
    This class `HBNBCommand` contains methods used for interpreting commands
    on the console
    """

    prompt = "(hbnb) "
    intro = "-------------Welcome to hbnb!-------------\n" + \
            "Enter \"help\" or \"?\" to get started\n"

    __classes = FileStorage().classes
    __cmds = ["all", "create", "update", "destroy", "show", "count"]
    __protected = ["id", "created_at", "updated_at"]

    def precmd(self, line):
        """Runs before the command line input is evaluated

        It is important for possibly refactoring our command line before
        returning it to `onecmd` which handles the evaluation of the line
        """

        line = line.lstrip(" ")
        match = re.search(r'^([a-zA-Z]+)\.([a-z]+)\(', line)
        if not match:
            return line

        class_name = match.group(1)
        if class_name not in HBNBCommand.__classes:
            return line

        cmd = match.group(2)
        if cmd not in HBNBCommand.__cmds:
            return line

        if cmd == "all" or cmd == "count":
            return self.handle_all_and_count(line, cmd, class_name)

        if cmd == "show" or cmd == "destroy":
            return self.handle_show_and_destroy(line, cmd, class_name)

        if cmd != "update":
            return line

        return self.handle_update(line, cmd, class_name)

    def handle_all_and_count(self, line, cmd, class_name):
        """Handles the `all` and `count` extensions in classes

        Args:
            line (str): Command line
            cmd (str): Command entered
            class_name (str): Class name referenced

        Returns:
            line (str): The original command line, usually returned if an error
                occured a mismatch was found
            arg (str): A refactored command line to pass to an existing command
                or a new line if the extension was `count`
        """

        match = re.search(r'\(\)', line)
        if not match:
            return line

        arg = "{} {}".format(cmd, class_name)
        if cmd == "count":
            self.count(arg)
            arg = "\n"

        return arg

    def handle_show_and_destroy(self, line, cmd, class_name):
        """Handles the `show` and `destroy` extensions in classes

        Args:
            line (str): Command line
            cmd (str): Command entered
            class_name (str): Class name referenced

        Returns:
            line (str): The original command line, usually returned if an error
                occured a mismatch was found
            arg (str): A refactored command line to pass to an existing command
        """

        match = re.search(r'\(["\'](.+)["\']\)', line)
        if not match:
            return line

        instance_id = match.group(1)
        arg = "{} {} {}".format(cmd, class_name, instance_id)

        return arg

    def handle_update(self, line, cmd, class_name):
        """Handles the `update` extension in classes

        Args:
            line (str): Command line
            cmd (str): Command entered
            class_name (str): Class name referenced

        Returns:
            line (str): The original command line, usually returned if an error
                occured a mismatch was found
            arg (str): A refactored command line to pass to an existing command
                or a new line if `onecmd` executes successfully
        """

        match_regular = re.search(
            r'\(["\'](.+)["\'],\s*["\'](.+)["\'],\s*(.*)\)', line)
        match_dict = re.search(r'\(["\'](.+?)["\'],\s*(\{.+\}?)\)', line)
        if not match_regular and not match_dict:
            return line

        quotes = ["'", '"']
        if match_regular:
            instance_id = match_regular.group(1)
            attr_name = match_regular.group(2)
            attr_value = match_regular.group(3)
            if attr_value[0] not in quotes and attr_value[-1] not in quotes:
                attr_value = '"{}"'.format(attr_value)

            arg = "{} {} {} {} {}".format(
                cmd, class_name, instance_id, attr_name, attr_value)

            return arg

        instance_id = match_dict.group(1)
        attr_dict = match_dict.group(2)
        try:
            attr_dict = json.loads(attr_dict)
        except (ValueError, TypeError):
            try:
                attr_dict = re.sub("'", '"', attr_dict)
                attr_dict = json.loads(attr_dict)
            except (ValueError, TypeError):
                return line

        for key, value in attr_dict.items():
            value = '"{}"'.format(value)
            arg = "{} {} {} {} {}".format(
                cmd, class_name, instance_id, key, value)
            self.onecmd(arg)
        arg = "\n"

        return arg

    def count(self, arg):
        """Prints the number of instances of a class

        Args:
            arg (str): A refactored version of the original command line
        """

        args = arg.split()
        print(len([obj for obj in storage.all().values()
              if type(obj).__name__ == args[1]]))

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
            return

        args = arg.split()
        classname = args[0]
        if classname not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        attrs = {}
        for arg in args[1:]:
            # find a quote/unquote string, a float, or an integer
            match = re.match(r'^([\w]+)=(\".*?\"|\d+\.\d+|\d+)$', arg)

            # invalid arguments should be skipped
            if not match:
                continue

            key, value = match.groups()
            if key in HBNBCommand.__protected:
                print("** cannot set {} manually".format(key))
                continue

            if value.startswith('"'):
                # string values will contain underscore instead of spaces and
                #  should be replaced appriopriately
                value = value[1:].replace('_', ' ')

                # if lines end with backslash then user needs more space
                while value.endswith('\\'):
                    value = value[:-1] + ' ' + input().strip()

                # all escaped double quotes within the value should be replaced
                value = value[:-1].replace('\\"', '"')
            elif '.' in value:
                value = float(value)
            else:
                value = int(value)

            attrs[key] = value

        instance = HBNBCommand.__classes[classname](**attrs)
        instance.save()
        print(instance.id)

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

        if not arg:
            print("** class name missing **")
            return

        match = re.search(r'"(.*)"', arg)
        if match:
            attr_val = match.group(1)

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
        if attr_name in HBNBCommand.__protected:
            print("** cannot update {} attribute **".format(attr_name))
            return

        if len(args) == 3:
            print("** value missing **")
            return

        attr_value = self.vet_attr_value_in_update(match, obj, args, attr_val)
        # if hasattr(obj, attr_name):
        if not attr_value:
            return

        setattr(obj, attr_name, attr_value)
        obj.save()

    def vet_attr_value_in_update(self, match, obj, args, attr_val):
        """Verify attribute name to set in case of quotations when using update

        Args:
            match (str): String returned by re
            obj (obj): The instanc of the class to be updated
            args (str): List of arguments split from the command line
            attr_val (str): Potential value gotten from within the quotations

        Returns:
            attr_value (str): The final value set
        """

        attr_name = args[2]
        if match and args[3][0] == '"':
            attr_value = attr_val
        else:
            attr_value = args[3]

        try:
            attribute = getattr(obj, attr_name)
            try:
                attr_type = type(attribute)
                attr_value = attr_type(attr_value)
            except ValueError:
                print("** {} expects a value of type '{}' **".format(
                    attr_name, attr_type.__name__))
                return

        except AttributeError:
            try:
                attr_value = int(attr_value)
            except ValueError:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass

        return attr_value

    def help_EOF(self):
        """Prints help for the EOF command"""

        print("Exits the program when it receives an EOF signal\n")

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
