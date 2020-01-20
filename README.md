## EBM DataLab Teaching Resources

### Table of contents
- [Git and Github](#git-and-github)
    + [Make a github account](#make-a-github-account)
    + [Install git](#install-git)
    + [Clone a repository](#clone-a-repository)
    + [Make a branch](#make-a-branch)
    + [Make change and commit](#make-change-and-commit)
    + [Create a pull request](#create-a-pull-request)
- [Repo Structure](#repo-structure)
  * [Notebooks](#notebooks)
  * [Code](#code)
  * [Data](#data)
  * [Tests](#tests)
- [Installing new packages](#installing-new-packages)

### Git and Github

We have the team github [here](https://github.com/ebmdatalab). 

##### Make a github account 

Sign up at [github.com](https://github.com/). You will need to be added to the EBM Datalab or git repo you want to use by a member of our team. 

##### Install git 

For Macs: Go [here](https://git-scm.com/downloads) and follow the instructions. You will need to install Xcode Tools via the app store to get this to work.

For Windows: Go [here](https://git-scm.com/downloads). 

##### Clone a repository

Go to the command line (Terminal on Mac, Powershell in Windows is best). You will now clone a repo onto your computer. This involves making a file using the command line. It is best to navigate to a place on your computer where you want this to be. Remember your basic command line commands:

```cd [directory-name]``` to change directory

```cd .. ``` to go up to a parent directory

```ls ``` list contents in your current directory

```pwd ``` print your working directory

```mkdir [new-directory-name] ``` to make a directory 

Then we need to clone the repo into our current working directory. Do this command:

```git clone [your.repo]```

For example, if you wanted to clone this repo, you do:

```git clone https://github.com/CarolineMorton/educationresource.git```

If you want to clone another repo, locate the green clone button on the front page of the repo and copy from here. It should always end in .git. 

##### Make a branch 

All repos will have a master branch. It may also have some extra branches that people have used in the past. We want to avoid merging our work directly with the master branch incase it causes errors, therefore it is better to checkout a new branch. To do this:

```git checkout -b [branch-name]```

for example, we could do a branch called feature1

```git checkout -b feature1```

This means that we have created a new branch on our local machine called ```feature1```

##### Make change and commit 

We are then free to add, change or delete files as we see fit. To see any changes do:

```git status```

Once you are ready to send back to github and share more widely you will need to do 3 steps. 

```git add . ``` - this adds any changes 

Then we can commit with a message. We have written some instructions on commit messages [here](https://docs.google.com/document/d/1LD5hVjFOWx1AptbXkdTS135ureLkxd8kCumgl8mxzaA/edit#)
in the git section. 

```git commit -m "add your message here```

You can choose to force users to write longer more detailed git commit messages. This helps with auditing and understanding how a
code base is growing. You can see [here](https://thoughtbot.com/blog/better-commit-messages-with-a-gitmessage-template) how
to set up a git commit template. An example is in this repo to give you a favour of how this works. 

We can repeat add and commit if we are working on a project and want to store checkpoints. 

Finally we push to a branch. 

```git push origin [branch-name]```

Sometimes this will result in a clash. This is usually because someone else has pushed to the branch in the time you 
have been working on it. 

If this is the case, you will need to ```git pull``` their work into your local machine, resolve all clashes, recommit and then push. 

Git has a useful cheatsheet of commands [here](https://www.git-tower.com/blog/git-cheat-sheet/)

##### Create a pull request

It is good practice to get your code checked before you merge your branch with the master branch. To do this create a pull request. 

If you log into your github account in the browser. You could now see a prompt for 'create pull request'. Click this and nominate a reviewer or reviewers. They will check it and merge into the master, make changes or comment on your code. 



### Repo Structure

Each repo will have this basic folder structure. For more information, please see our [Open Analytics Manifesto](https://docs.google.com/document/d/1LD5hVjFOWx1AptbXkdTS135ureLkxd8kCumgl8mxzaA/)

```bash
├── code
│   └── custom_functions.py  
├── config                    
│   └── jupyter_notebook_config
├── data
├── notebooks
├── tests
├── .gitattributes
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.in
├── requirements.txt
├── run.bat
├── run.sh
└── run_tests.sh

```

#### Notebooks
By convention, all Jupyter notebooks live in `notebooks/`.  Notebooks now run via JupyterLab and will appears to have a 
slightly different structure, with a sidebar showing the directory tree on the left hand side. 

See our [manifesto guidelines](https://docs.google.com/document/d/1LD5hVjFOWx1AptbXkdTS135ureLkxd8kCumgl8mxzaA/) on notebooks best practice. 

#### Code

When notebooks look like they will contain more than a few lines of Python,
the Python is separated into a separate module, in `code/`, and
imported from the notebook.

This will require you to path to the right file from within your notebook. For this to work 
you need to have an empty \_\_init\_\_.py within your code folder. 

There are 2 ways of getting your code into your notebook. The best way is to add an import statement at the top of your notebook and import the functions individually. For example: 

```python
from code.custom_functions import multiplier
```

Alternatively you can import all contents of your file. 

```python
from code import custom_functions
```

See the example in this repo and work through the example in `notebooks/notebook_importing_code`

#### Data

Data, including raw and processed data, should be stored within the `data/` folder.  You can easily import data (such as CSV or JSON) from within your own directory; but this would mean that
all data has to be kept within your notebooks folder. Paths can be created easily with 
the `os` module. It is a good idea to make a variable called filename which contains the name of the data file you would like to path to:

```python
filename = "data_file.csv"
```

We use two inbuilt functions of the `os` module to path to the right folder (a sister folder of notebooks called data) 

This command returns the current working directory:
```python
os.getcwd()
```

This command allows you to go up a level to a higher directory: 
```python
os.path.dirname()
```

By combining them, you get to the parent directory of your current working directory. You can then add on the name of the folder `data`
to path to the correct location of the data:

```python
path = os.path.dirname(os.getcwd()) + "/data/" + filename
```

If you print path, you will now get, something like:

```bash
'/Users/carolinemorton/Documents/ebmdatalab/data/data_file.csv

```

You could choose to add 2 folders to the `data/` folder called `/raw_data` and `/processed_data` to make it easy to read. 

See the example in this repo and work through the example in `notebooks/notebook_importing_data`

#### Tests

Tests live in `tests/` folder. Tests are run automatically with [pytest](https://docs.pytest.org/en/latest/). This library
will find any python files called `test_*.py` and then find any functions called `test_*()`.   

The standard format is that you have one test function for each function. There are number of ways of doing tests but probably
the cleanest way is to reimplement your code in a new way and test the results. 

See the example in this repo and work through the example in `tests/test_custom_functions`. The function is called 
`test_sum_values()` and is reimplementation of a function called `sum_values()`. This was taken from [here](https://realpython.com/python-testing/#testing-your-code). 

Any test function needs to `assert` its output is the same at the function output. See more about `assert` [here](https://www.w3schools.com/python/ref_keyword_assert.asp). 

You then run the test from the command line:
```bash
python -m pytest
```

You should get something that looks like this:

```bash
Carolines-MacBook-Air-3:teaching_resource carolinemorton$ python -m pytest
============================ test session starts =============================
platform darwin -- Python 3.6.8, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: /Users/carolinemorton/Documents/ebmdatalab/teaching_resource, inifile:
collected 1 item                                                             

tests/test_custom_functions.py .                                       [100%]

========================== 1 passed in 0.02 seconds ==========================
```

### Installing new packages

Best practice is to ensure all your python dependencies are pinned to
specific versions. To ensure this, while still supporting upgrading
individual packages in a sane way, we use
[pip-tools](https://github.com/jazzband/pip-tools).

The workflow is:

* When you want to install a new package, add it to `requirements.in`
* Run `pip-compile` to generate a `requirements.txt` based on that file
* Run `chmod 777 requirements.txt` . The newly generated requirements.txt has specific requirements which don't intergrate 
well with Docker. We need to run this command to open all the requirements. For more info on this specific command see [here](https://www.dreamvps.com/wp-content/uploads/2018/03/output_1520884742.htm) 
* Run `pip-sync` to ensure your installed packages exactly match those in `requirements.txt`
* Commit both `requirements.in` and `requirements.txt` to your git repo

To *upgrade* a specific package:

    pip-compile --upgrade-package <packagename>

To upgrade everything:

    pip-compile --upgrade

Don't forget to run `pip-sync` after running
any upgrade command.

To execute these within your dockerised environment, start a new Bash
console in Jupyter Lab (from the same menu you would create a new
notebook).

You can then run whatever shell commands you like, by typing them and
hitting Shift + Enter to execute.
