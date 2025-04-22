# quespaper_generator
The code is a Python program that uses the tkinter library to create a GUI application for generating question papers. It also interacts with a MySQL database to store and retrieve information about the question papers.
The question paper follows a pattern of all subjective questions divided into three sections.

The program consists of several classes and functions:

1. The `windows` class is the main display class that creates the initial window with various options like adding questions, generating papers, and adding subjects.

2. The `add`, `generator`, and `add_sub` methods within the `windows` class are responsible for handling the functionality of adding questions, generating papers, and adding subjects, respectively.

3. The `question_paper` class is used to extract questions from the database and generate question papers based on the specified criteria.

4. The `preview` class is used to display a preview of the question paper before generating it.

5. The `done` function creates a new window with options to generate or preview the question paper.

6. The `get` and `start` functions are used for handling the login process to connect to the MySQL database.

The program uses various tkinter widgets such as buttons, labels, entry fields, and canvas to create the GUI interface. It also uses the PIL library to work with images and the mysql.connector library to interact with the MySQL database.
