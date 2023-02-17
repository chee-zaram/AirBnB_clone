## Testing

Unittests for all components of the application are well written and documented, and are contained
in this directory.

You can run tests for all components of the application by using the following
command from the root of the project repository:

```sh
python3 -m unittest discover tests
```

Alternatively, you could specify which component to run tests on by using the following format:

```sh
python3 -m unittest path/to/testfile
```

where `path/to/testfile` is the relative path to the file containing tests.
