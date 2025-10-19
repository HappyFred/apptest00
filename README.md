# Simple App Demo

*TO READ THIS FILE IN VS CODE:  
**View** > **Command Palette** > **Markdown: Open Preview to the Side** (type this in the box)*

---

## Overview

This is a *very* simple Flask + MySQL web app.  
It shows the basics of each of the main types of Flask app page without complications to cause errors or distractions:  
-  It has a simple `people` table with 3 columns in the `simpleapp` database
-  One page lists all people (`SELECT` query) with unique Details link for each person
-  Person detail page (`SELECT` query using a `%s` marker) and Edit link
-  Edit person detail page (form loads person data, sends edits using `POST` method)
-  Add person page (blank form, sends data using `POST` method)

## How to Install this Demo

1. **Create database:**   
In MySQL Workbench, run `simpleapp-local.sql`. This will create the `simpleapp` database.
    - Open the file from *inside* Workbench (opening the file from Explorer/Finder won't work)
    - After running the query, press 🔄 Refresh arrows in the top right of the **Schemas** sidebar to see it in the list.
2. **Enter your MySQL password:**   
In `connect.py` change `'your_password_here'` to your actual MySQL password.
3. **Create virtual environment**  
In VS Code: **View** > **Command Palette** > **Python: Create environment** > **Venv** > **Python version** >  **☑ requirements.txt**  
(`requirements.txt` preinstalls Flask and the MySQL client for you when you create the virtual environment.)
4. **Run the app:**  
To run with debugging:  **Run** > **Start Debugging** > **Python Debugger** > **Flask** (<u>NOT</u> *Python file*!) > **app.py**  
Go to http://127.0.0.1:5000 in your browser to view the app.


## Project Structure

### HTML Pages 

#### 0. Base Template
- `base.html` - Creates page header with title and menu. All pages extend this template

#### 1. Home Page
- `home.html` - Display simple plain text home page

#### 2. List People
- `person_list.html` - Lists person details for all people

#### 3. Person Details (from List People link)
- `person.html` - Display all details for a person

#### 4. Edit person (from Person Details link)
- `person_edit.html` - Edit details for a person

#### 5. Add person (from List People link)
- `person_add.html` - Enter details for a new person


### Route Classification (by menu order)

#### 1. Home Page Routes
| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Display home page |

#### 2. Person Management Routes
| Route | Method | Description |
|-------|--------|-------------|
| `/person_list` | GET | Display list of people |
| `/person` | GET | Display person details |
| `/person_edit` | GET | Person details in editable form |
| `/person_update` | POST | Save person edits. Redirect to person details. |
| `/person_add` | GET | Display empty person details form |
| `/person_insert` | POST | Insert new person details. Redirect to new person details. |

