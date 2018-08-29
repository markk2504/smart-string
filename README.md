# Smart String
Smart String is a Python 2.7 library to correctly parse code points (Unicode symbols with assigned  
numeric value) in the Unicode basic multilingual plane (BMP) or in the supplementary multilingual  
planes, and to form characters that consist of more than one code point.  

### Using the Smart String Library
The Smart String library exposes 3 main classes - `CodePoint`, `SmartChar`, and `SmartStr`.  
The `CodePoint` class represents a single Unicode code point, either in the BMP or in the supplementary  
planes.  
The `SmartChar` class represents a single graphical character. It can consist of 1 code point (letter  
in the English Alphabet), or 2 code points (national flag symbol).  
The `SmartStr` class represents a string containing a sequence of smart characters.  

### Running the example code
Go to the location of the example file in a terminal and run the example script.  
`cd <smart-string package location>/smart_str/example`  
`python smart_str_example.py`  

### Running the tests
To run the tests make sure that the pytest package is installed on your system.  
Go to the location of the tests directory in a terminal and run the tests. You can run all the tests in  
the tests directory, all the tests in a single module, or a single test in a module.  
`cd <smart-string package location>/smart_str/tests`  
`pytest .` - Run all the tests in the tests directory.  
`pytest test_code_point.py` - Run all the tests in a single module.  
`pytest test_code_point.py::test_code_point_utf_8_four_bytes` - Run single test in a module.  
