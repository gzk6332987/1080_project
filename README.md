# 1080_project

## <span style="color: red;">IMPORTANT NOTE<span>

### We suggest you run `script\pull_latest.bat` (for windows user) or `script/pull_latest.sh` (for mac and linux user) to pull the latest version from github

### For windows user, please run `run.bat` or `run.ps1` 

### For mac and linux user, please run `run.sh`


### Python version must be 3.11+, there are some lib only exist in these version

<br>
<br>

---

## Project Description

Mathematics is a common challenge faced by primary students. Owing to weak understanding of mathematical principles, underachieving students usually receive unsatisfied academic results in mathematics, aggravating students’ academic pressure, and teachers’ workload. Moreover, insufficient basic mathematics skills are unfavorable to their education in their future secondary school life. To solve these problems, a tool was created, namely Mathematics Educational Game, aiming at enhancement of students’ mathematical ability. 

## Reflection 

Currently, one table will be created for every account creation to record the results of every account, leading to data redundancy, leading to insufficient file compression. Moreover, there is no graphical interface for users to access the data in database for reviewing their attempts, bringing inconvenience to users. 

## Program Principle

### Enter
When you run `script\pull_latest.sh`or `script/pull_latest.sh`, it will pull latest version from github, make it always up to date.

When you run `run.sh`, `run.ps1`, or `run.sh`, it will automatically active virtual environment and run main.py (:

### Initialize
We use `config.toml` file set some basic setting, in python code, we use toml lib read all config into `InitializeInfo` class

### Mistake Question
We use sqlite to log students failed problems, when student failed to answer same mistake question, `mistake_count` (a variable in database) will be added, when student successfully answer the correct answer, `mistake_count` will be deducted, and the program will show the same problem for several times until `mistake_count` reduce to zero

### GUI
We use PyQt5 as our program GUI engine, we use PyQt Designer app to design the GUI, use PyQt5 `.connect()` method connect GUI behavior and logic process. 

### Class Use
We separate each part through class, each part could maintain independently, make it easier to develop and debug!  (: 

### Additional Information: Git Usage

We use git to develop the program together, it also help use manage different version. We use `git commit -m "MESSAGE"` to submit each changes, use `git pull origin main` to synchronous program development

You can access github website *https://github.com/gzk6332987/1080_project* to review our project

You can use `git log --oneline --graph --all` show each commit and progress (:

You can use `git tag` show each version of our project (If you want, you can try each version, but not all success due to database structure problem) (:

### Additional Information: Open Source License

This project have Apache 2.0 License, if you have better suggestion or comments, feel free to submit it in github **issue** module