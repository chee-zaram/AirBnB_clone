# AirBnB Clone - The Console

---

![Last Commit][last_commit-badge]
[![Contributors][contributors-badge]][contributors]
[![License][licence-badge]][license]

---

This project is the first stage in an attempt to clone the popular vacation rental platform,
[AirBnB](https://airbnb.com).
The end-goal of the project is to build a full-fledged system for managing vacation rentals,
including features for users to list their properties, make bookings, and manage their reservations.
However, for this specific project, we will be attempting to build the console.

This particular project uses a file storage style database, but will be upgraded to use
[MySQL](https://mysql.com) in the future.

## Getting Started

Clone this git repository. If you are a GNU/Linux user, you could copy and paste the
following command to clone and change working directory into the root of this project:

```sh
git clone https://github.com/chee-zaram/AirBnB_clone.git && cd AirBnB_clone
```

other wise, clone the repository as you'd like and change working directory into
the root of the project.

## Command Interpreter

The command interpreter is a command-line interface that allows users to interact
with the **AirBnB** clone system. It provides a set of commands for managing the various
aspects of the system, such as creating and managing listings, managing bookings, and so on.

### Starting the Command Interpreter

To start the command interpreter, navigate to the root of the project if not already there
and run the following command:

```sh
./console.py
```

This will start the command interpreter and you will be presented with a prompt,
`(hbnb) `, where you can start entering commands.

### Using the Command Interpreter

The command interpreter provides a set of commands for managing the various aspects
of the **AirBnB** clone system. Some of the available commands include:

| Command   | Description                                                       | Usage                                                                 |
| --------- | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| `create`  | Create a new instance of a class                                  | `create <class_name>`                                                 |
| `show`    | Show the details of a specific instance of a class                | `show <class_name> <instance_id>`                                     |
| `all`     | Display the details of all instances, or all instances of a class | `all` or `all <class_name>`                                           |
| `destroy` | Delete a specific instance of a class                             | `destroy <class_name> <instance_id>`                                  |
| `update`  | Update the attribute value for a given instance of a class        | `update <class_name> <class_id> <attribute_name> "<attribute_value>"` |
| `quit`    | Quits the command interpreter                                     | `quit`                                                                |

> The interpreter can also be terminated by hitting `EOF` key combination.

To use a command, simply type the command followed by any required arguments at the prompt
and hit enter.

For example, to create a new instance of the `User` class, you would run the following command:

```sh
(hbnb) create User
```

To show the details of a specific instance of a class, you would run the following command,
where `<class_id>` is the ID of the instance you want to show:

```sh
(hbnb) show User <class_id>
```

Some interpreter commands can also be processed when used as suffixes to a class name:

- `show`: `<class_name>.show("<instance_id>")`

Example:

> ```sh
> (hbnb) User.show("1234-5678")
> ```
>
> to print a representation of the user with id `1234-5678`

- `count`: `<class_name>.count()`

Example:

> ```sh
> (hbnb) BaseModel.count()
> ```
>
> to get the number of instances of the class `BaseModel`

- `all`: `<class_name>.all()`

Example:

> ```sh
> (hbnb) City.all()
> ```
>
> to print all instances of the class `City`

- `destroy`: `<class_name>.destroy("<instance_id>")`

Example:

> ```sh
> (hbnb) Place.destroy("1234-5678")
> ```
>
> to delete the instance of class `Place` with id `1234-5678`

- `update`: `<class_name>.update("<instance_id>", "<attribute_name>", <"attribute_value">)`

Example:

> ```sh
> (hbnb) State.update("1234-5678", "name", "New York")
> ```
>
> to update the attribute called `name` of the instance of `State` class with id `1234-5678`

The `.update` extension also works with a dictionary of attribute name(s) and value(s)

Example:

> ```sh
> (hbnb) User.update("1234-5678", {"email": "airbnb.clone@airbnb.com", "password": "09876airbnb"})
> ```
>
> to update the email and password of the user with id `1234-5678`

For a full list of all commands and their usage, run the following command:

```sh
(hbnb) help
```

or

```sh
(hbnb) help <command>
```

for a help doc on a specific command.

## Authors

The [AUTHORS](https://github.com/chee-zaram/AirBnB_clone/blob/main/AUTHORS)
file at the root of the repository lists all individuals who were part of the project
from conception. They are also listed below as follows:

[Chee-zaram Okeke](github.com/chee-zaram) ecokeke21@gmail.com

[Yusuf-R](github.com/Yusuf-R) y.abdulwasiu@gmail.com

## Contributors

This lists all persons who have contributed to the project and can be found in the
[CONTRIBUTORS](https://github.com/chee-zaram/AirBnB_clone/blob/main/CONTRIBUTORS) file.

[licence-badge]: https://img.shields.io/github/license/chee-zaram/AirBnB_clone
[license]: https://github.com/chee-zaram/AirBnB_clone/blob/main/LICENSE
[contributors-badge]: https://img.shields.io/github/contributors/chee-zaram/AirBnB_clone
[contributors]: https://github.com/chee-zaram/AirBnB_clone/blob/main/CONTRIBUTORS
[last_commit-badge]: https://img.shields.io/github/last-commit/chee-zaram/AirBnB_clone
