This project will use a virtual environment directory, venv.
venv is a file containing tools that allow us to use the same versions of modules specified in requirements.txt

venv is not saved on the repository. I have added it to the '.gitignore'. This helps us avoid source control issues.

For this reason, you must set up the venv yourself to run dopestDish. (Assuming pip is installed.)
do this using the following steps:
	1. clone the repository to a local directory and navigate (cd) into it using command line
	2. the project folder will contain this README and requirements.txt (check with "dir" or "ls")
	3. from here, the Windows command for creating virtual env is "python -m venv venv/"
	4. to activate venv on Windows, use "venv\Scripts\activate"
	5. After activation, the commandline will start with "(venv)"
	   *to deactivate, simply type "deactivate"
	6. Make sure the venv is activated and write "pip install -r requirements.txt"

Now your virtual environment with the current versions of each module used for the project will be installed.
To check the list of modules being used, type "pip freeze" or "pip list"
The result of this command will be different based on whether your virtual environment is activated.
