<h1>File Integrity Monitor in Python</h1>

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

<br /><br /><b>Option 'B':</b>

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
<img src="https://i.imgur.com/v5ls9Db.png" height="80%" width="80%" alt="Run the Program"/>

<p align="center">
Launch the utility: <br/>

<br />
<br />
Select the disk:  <br/>
<img src="https://i.imgur.com/tcTyMUE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the number of passes: <br/>
<img src="https://i.imgur.com/nCIbXbg.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Confirm your selection:  <br/>
<img src="https://i.imgur.com/cdFHBiU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Wait for process to complete (may take some time):  <br/>
<img src="https://i.imgur.com/JL945Ga.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sanitization complete:  <br/>
<img src="https://i.imgur.com/K71yaM2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Observe the wiped disk:  <br/>
<img src="https://i.imgur.com/AeZkvFQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
