
## Authors

- [Mohammad Faraz Khan](https://github.com/mohammadfarazk)
- [Mason Garcia](https://github.com/MasonGarciaDev)
- [Kayla Baker](https://github.com/kaylambaker)
- [Daniel Lau](https://github.com/DLau02)
- [Yuya Cho](https://github.com/Yuya216)
- [Sid Goteti](https://github.com/Gotetisid)


## Installation

This project uses python for the GUI and MySql for the database. 

To download and install python, visit:
https://www.python.org/downloads/

To download and install Customtkinter, follow along the instructions:
- Open command prompt
- run the command: pip install customtkinter

To download and install MySql, visti:
https://dev.mysql.com/downloads/installer/

Next, download the project with git or extract the zip file to the desired directory 

```
https://github.com/DLau02/Database-Project.git
```


    
## Deployment

The MySql database must be initialized once before using the GUI program

Create a new database connection in MySql Workbench with the desired credentials

edit "gui/dbConfig.py" to match the credentials and  connection info in the previous step

open the database connection then navigate to file > Run Sql Script (click)

In the project files you have download select "Create tables and populate.sql"

The database is now initialized

Next, in a terminal, navigate to the projects gui directory and run  

```python
  python main.py 
```

The program will now open and features a simple menu system with descriptive titles for all options. 
