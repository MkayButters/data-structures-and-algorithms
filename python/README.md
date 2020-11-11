# Data Structures and Algorithms

## Language: `Python`

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`

### Table of contents

 1. [CC 01](code_challenges/array-reverse)
 2. [CC 02](code_challenges/array_shift)
 3. [CC 03](code_challenges/)
 4. [CC 04](code_challenges/)
 5. [CC 05](code_challenges/)
 6. [CC 06](code_challenges/)
 7. [CC 07](code_challenges/)
 8. [CC 08](code_challenges/)
 9. [CC 09](code_challenges/)
 10. [CC 10](code_challenges/)
 11. [CC 11](code_challenges/)
 12. [CC 12](code_challenges/)
 13. [CC 13](code_challenges/)
 14. [CC 14](code_challenges/)
 15. [CC 15](code_challenges/)
 16. [CC 16](code_challenges/)
 17. [CC 17](code_challenges/)
 18. [CC 18](code_challenges/)
 19. [CC 19](code_challenges/)
 20. [CC 20](code_challenges/)
 21. [CC 21](code_challenges/)
 22. [CC 22](code_challenges/)
 23. [CC 23](code_challenges/)
 24. [CC 24](code_challenges/)
 25. [CC 25](code_challenges/)
 26. [CC 26](code_challenges/)
 27. [CC 27](code_challenges/)
 28. [CC 28](code_challenges/)
 29. [CC 29](code_challenges/)
 30. [CC 30](code_challenges/)
 31. [CC 31](code_challenges/)
 32. [CC 32](code_challenges/)
 33. [CC 33](code_challenges/)
 34. [CC 34](code_challenges/)
 35. [CC 35](code_challenges/)
 36. [CC 36](Reading_files/class36.md)
 37. [CC 37](Reading_files/class37.md)
 38. [CC 38](Reading_files/class38.md)
 39. [CC 39](Reading_files/class39.md)
 40. [CC 40](Reading_files/class40.md)
 41. [CC 41](Reading_files/class41.md)
 42. [CC 42](Reading_files/class42.md)
 43. [CC 43](Reading_files/class43.md)
 44. [CC 44](Reading_files/class44.md)
 45. [CC 45](Reading_files/class45.md)
