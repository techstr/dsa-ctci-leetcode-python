# Study Python Project

This repository contains Python code for leetcode problems and data structures. Included Jupyter Notebooks for easy coding and testing on single file. All unit test cases are based on pytest. Follow the instructions below to set up your development environment using Visual Studio Code (VS Code) and create a Python virtual environment.

---

## Prerequisites

Before starting, ensure you have the following installed on your system:
- [Python (3.7 or later)](https://www.python.org/downloads/)
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
- [pip](https://pip.pypa.io/en/stable/) (comes with Python)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (optional, but recommended)

---

## Setting Up VS Code for Python Development

1. **Install the Python Extension**:
   - Open VS Code.
   - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or pressing `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux).
   - Search for "Python" and install the official extension by Microsoft.

2. **Select the Python Interpreter**:
   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) to open the Command Palette.
   - Type `Python: Select Interpreter` and select it.
   - Choose the Python interpreter you want to use (e.g., the one installed on your system or a virtual environment).

3. **Install Additional Extensions (Optional)**:
   - Install extensions like `Pylance` for better IntelliSense and `Black Formatter` for code formatting.

---

## Creating a Python Virtual Environment

1. **Open the Terminal in VS Code**:
   - Go to the Terminal menu and select `New Terminal` or press ``Cmd+` `` (Mac) or ``Ctrl+` `` (Windows/Linux).

2. **Create a Virtual Environment**:
   - Run the following command in the terminal:
     ```bash
     python -m venv venv
     ```
   - This will create a virtual environment in a folder named `venv`.

3. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Verify the Virtual Environment**:
   - After activation, the terminal prompt should show `(venv)` at the beginning.
   - Run the following command to verify:
     ```bash
     python --version
     ```

---

## Installing Dependencies from [requirements.txt](http://_vscodecontentref_/1)

1. **Ensure the Virtual Environment is Activated**:
   - Follow the steps above to activate the virtual environment.

2. **Install Dependencies**:
   - Run the following command in the terminal:
     ```bash
     pip install -r requirements.txt
     ```

3. **Verify Installation**:
   - Run the following command to list installed packages:
     ```bash
     pip list
     ```

---

## Running the Project

1. **Activate the Virtual Environment**:
   - Ensure the virtual environment is activated.

2. **Run Python Scripts**:
   - Use the terminal or VS Code's Run feature to execute Python scripts:
     ```bash
     python script_name.py
     ```

3. **Run Tests**:
   - If the project includes tests, you can run them using `pytest`:
     ```bash
     pytest
     ```

---

## Additional Notes

- **Formatting Code**:
  - Use the `Black` formatter to format your code. You can configure it in VS Code or run it manually:
    ```bash
    black .
    ```

- **Linting**:
  - Use `pylint` or `flake8` for linting:
    ```bash
    pylint script_name.py
    ```

- **Deactivating the Virtual Environment**:
  - To deactivate the virtual environment, run:
    ```bash
    deactivate
    ```

---

## Troubleshooting

- If VS Code does not detect the virtual environment, restart VS Code and reselect the Python interpreter (`Python: Select Interpreter`).
- Ensure [requirements.txt](http://_vscodecontentref_/2) is up-to-date with all necessary dependencies by running:
  ```bash
  pip freeze > requirements.txt