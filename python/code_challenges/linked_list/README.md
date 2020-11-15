# Singly Linked List
<!-- Short summary or background information -->
Creating a list and tests to test for it

## Challenge
<!-- Description of the challenge -->


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach i took was breaking down each section and building it into a whole working product. The big O for time is O(1) because no matter how many nodes you add it will always take the same amount of time to run because it reads the head of the list of nodes.

## API
<!-- Description of each method publicly available to your Linked List -->
- A Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- LinkedList class, includes a head property. Upon instantiation, an empty Linked List is created.
- A method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
- A method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
- A method called __str__  which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

#### __Tests__

1. Can successfully instantiate an empty linked list
2. Can properly insert into the linked list
3. The head property will properly point to the first node in the linked list
4. Can properly insert multiple nodes into the linked list
5. Will return true when finding a value within the linked list that exists
6. Will return false when searching for a value in the linked list that does not exist
7. Can properly return a collection of all the values that exist in the linked list
