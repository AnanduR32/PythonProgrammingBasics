# Python Basics
This repository contains most of the basic programs taught early on in academia for python language.

## Data Structures 
* ### Built-in 
    * **Lists**: 
        * Can contain heterogenous data
        * Initialized using square brackets
        * Is mutable, new data can be appended, values can be removed and so on
    * **Tuple**:
        * Heterogenous data
        * Initialized using parenthesis
        * Is immutable
        * Faster than lists
    * **Dictionary**
        * Store data using key:value pairs
        * They are mutable
        * Initialized using curly brackets where the key:value pair is specified
        * Data is added to dictionary simply by specifying a new key and assigning a value to it, dict[key] = value
    * **Sets**
        * Unordered collection of unique elements
        * Sets are mutable 
        * can perform various actions that are possible in algebraic sets such as union, difference, intersection and so on
* ### User Defined
    * **Array**
        * Similar to lists but can store only homogenous data
    * **Stack**
        * Linear 
        * Based on principle of LIFO
        * With 'Top' as reference can perform various activities such as push, pop, and access.
        * Used in recursive programming, undo mechanisms in word editors, reversing strings, etc.
    * **Queue**
        * Linear
        * FIFO
        * Has operations that can be performed from both ends of the data structure built upon the principle of arrays, the two ends are refered to as 'head' and 'tail'. The operations of adding and deleting elements from the queue are called enqueue and dequeue respectively.
        * Used as network buffers of network traffic management, Operating system job scheduling and so on. 
    * **Tree**
        * Non-Linear
        * Comprises of roots, from where data originates, and nodes, other data points available to us
        * The node that precedes is the parent node, and the node that is after is called the child
        * The last nodes are called as leaf nodes.
        * Trees provide a hierarchy that can be used in various real world applications such as HTML pages, Json files and so on. It can also be used to make search operations much faster.
    * **Linked Lists**
        * Linear 
        * The data points are not continous and are linked to each other using pointers. In the basic type of linked list a node comprises of just the data and a pointer 'next' which points to the next node.
        * Most widely used in image viewing, music player applications and so on.
    * **Graph**
        * Store a data collection of points called as vertices and edges 
        * Most approximate representation of the realworld maps
        * Used to find cost to distance between the various datapoints called nodes, and hence find the least path, used by Google Maps, Uber, to find the least distance between two points on the map to reduce time of travel for the end-users.
    * **Hash Maps**
        * Similar to dictionary 
        * The address or the index value of the data element is generated from a hash function
        * The hash mapping of the index makes accessing the data faster as the index value behaves as a key for the data value.
