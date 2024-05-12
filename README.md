# datafun-02-projsetup-
Data Fundamental Project 2 
Objective
Develop a Python module that demonstrates proficiency in loops, project folder creation using pathlib, and importing modules. This module should include reusable functions for creating sets of project folders based on various criteria.
   
1. Project Start
In your Python file, create a docstring with a brief introduction to your project.
     >  """Forlder creation module using pathlib and useable functions"""

3. Import Dependencies (At the Top, After the Introduction)
Organize your project imports near the top of the file, following conventions. For example, standard library imports first, then external library imports (we don't need any of these yet), then local module imports. Follow conventional package import organization. Import each package just once near the top of the file.

     > import pathlib
   
5. Define Functions for Folder Creation
  >a.Define reusable functions to create a series of project folders.
>  b.Each function should have a clear purpose, input parameters, and return values if applicable.
>  c.Include a docstring for each function to describe its behavior.
>  d.Use for in range(), for in list, and while loops to demonstrate different looping techniques.
>  e.Use a list comprehension to demonstrate transforming a list into a new list.
>  f.Use conditional branching to demonstrate different folder creation options, such as including options to force lowercase or remove spaces.

Specific functions to implement and the technique to demonstrate.
   >Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
>   Function 2. For Item in List: Develop a function to create folders from a list of names.
>   Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
>   Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).


6. Always Join Paths with Pathlib
In your code, use pathlib to join paths and create folders. Never use operating system-specific path symbols such as slashes, backslashes, or double back slashes. 

7. Define Main Function
Define a main() function to test the folder creation functions and demonstrate the use of imported modules.

Conditional Script Execution (at the end of the file)
Ensure the main function only executes when the script is run directly, not when imported as a module by using standard boilerplate code.

if __name__ == '__main__':
    main()
Module Design
The code should be clear, well-organized, and demonstrate good practices. Include comments and docstrings for clarity.

Evaluation Criteria
Functionality: The project should be functional and meet all requirements.
Documentation: The project should be well-written and well-documented.
Presentation: The project should be presented in a clear and organized manner.
Professionalism: The project sho





