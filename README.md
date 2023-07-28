<h1>Python File Integrity Monitor</h1>

<h2>Description</h2>
The main purpose of this File Intregity Monitor is to track changes to files in a specified directory called "Files" and notify the user about any modifications, deletions, or new file creations. 

Here's a brief description of what the program does:<br /><br />

It presents a user menu with two options:<br />

<b>Option 'A'</b>: Collect a new baseline of file hashes for the files in the "Files" directory.<br />
<b>Option 'B':</b> Begin monitoring files in the "Files" directory using the previously collected baseline.<br /><br />

<b>Option 'A':</b>
- The program calculates the SHA-512 hash for each file in the "Files" directory.
- It saves the file paths and their corresponding hashes into a file called "baseline.txt".
- This step establishes the initial baseline of the files in the directory.

<b>Option 'B':</b>

- The program loads the baseline information (file paths and hashes) from "baseline.txt" into a dictionary.
- It enters into a continuous monitoring loop that checks the files in the "Files" directory at regular intervals (every second).
- For each file in the "Files" directory, it recalculates the SHA-512 hash and compares it with the baseline hash stored in the dictionary.
- If a new file is created or if a file's content is modified, it notifies the user about the change.
- If a file that was present in the baseline has been deleted, it notifies the user about the deletion.
- The program uses the hashlib library to calculate SHA-512 hashes and the os library for file system operations.

To avoid repeating notifications for the same changes, it maintains a separate dictionary to keep track of the files for which notifications have already been shown.

Overall, this program helps users monitor the integrity of files in the "Files" directory and promptly detects any unauthorized modifications or deletions, providing an added layer of security to the data stored in the directory.
<br />

<h2>Flowchart</h2>
<img src ="https://i.imgur.com/XStwY3X.png" />

<h2>Languages Used</h2>

- <b>Python</b>

<h2>Program walk-through:</h2>

Before starting, Make sure that you have Python installed in your system. Open command prompt and change directory to where you downloaded the project. Then enter the command:<br />
```python fim.py```<br /><br />
<img src="https://i.imgur.com/v5ls9Db.png" height="80%" width="80%" alt="Run the Program"/><br /><br />

The program will launch and will give two choices:<br />

A. Collect new Baseline?<br />
B. Begin monitoring files with saved Baseline?<br /><br />
<img src="https://i.imgur.com/uC500ch.png" height="80%" width="80%" alt="Choices"/><br /><br />

<h3>Collect new Baseline</h3>
In the Python_FIM folder, there is another directory named "Files":<br /><br />
<img src="https://i.imgur.com/MxcoWlk.png" height="80%" width="80%" alt="Files Folder"/><br /><br />


Open the "Files" folder. Add any new files that you want to monitor. There are 3 pre-created text files in the folder. Add any new files in the folder which you would want to monitor:<br />
<img src="https://i.imgur.com/c9Qjnrg.png" height="80%" width="80%" alt="Files"/><br /><br />

When the files are added in the folder, go back to your command line. Enter ```A``` and press ```Enter```<br /><br />
<img src="https://i.imgur.com/kHFefnL.png" height="80%" width="80%" alt="Files"/><br /><br />

After pressing ```Enter```, The program will exit. In the program folder, the textfile named ```baseline.txt``` should include all the files with their SHA-512 hashes:<br /><br />
<img src="https://i.imgur.com/KKoXXqY.png" height="80%" width="80%" alt="Files"/><br /><br />

At this point, the baseline files are documented and are ready for monitoring. 

<h3>Begin Monitoring</h3>
Run the program again in the command line using ```python fim.py```.<br /><br />
<img src="https://i.imgur.com/beYHaD9.png" height="80%" width="80%" alt="Files"/><br /><br />

Enter ```B``` and press ```Enter```:<br /><br />
<img src="https://i.imgur.com/ZyYa30g.png" height="80%" width="80%" alt="Files"/><br /><br />
The file monitoring will start.

<h3>FIM Examples</h3>
<h4>Changing file content</h4>
In this example, I change the file content in ```textfile1.txt```. I added the words ```Changing Content!!!!!!``` in the start of the file. As soon as I save the file, the FMI alerts me that the file has been changed. <br />br />
<img src="https://i.imgur.com/Ej0cuUa.png" height="80%" width="80%" alt="Files"/><br /><br />
<img src="https://i.imgur.com/GiidRtk.png" height="80%" width="80%" alt="Files"/><br /><br />

<h4>Adding new files</h4>
In this example, I add another file to the ```Files``` folder. As soon as I save the file, the FIM alterts me that a new file has been created.<br /><br />
<img src="https://i.imgur.com/tdTsgxP.png" height="80%" width="80%" alt="Files"/><br /><br />
<img src="https://i.imgur.com/R1HEy1n.png" height="80%" width="80%" alt="Files"/><br /><br />

<h4>Delete a file</h4>
In this example, I delete the file named ```textfile2.txt```. As soon as I delete the file, the FIM alerts me that the file has been removed.<br />br />
<img src="https://i.imgur.com/RXez125.png" height="80%" width="80%" alt="Files"/><br /><br />
<img src="https://i.imgur.com/DBY0JRM.png" height="80%" width="80%" alt="Files"/><br /><br />

<h3>Stopping the Program</h3>

The program will continue to monitor the files until you stop it manually by pressing ```Ctrl+C``` in the terminal. If you want to start monitoring again later, you can rerun the program and choose option 'B' again. The program will use the previously collected baseline to continue monitoring the files.
<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
