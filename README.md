# Gmail Dot Trick Generator
This Python script generates all possible variants of an email address by inserting dots between characters in the username part. The generated variants are saved to a text file in the current directory.

# How to use
1. Clone or download this repository to your local machine.
2. Install Python 3.x if you haven't already.
3. Open a command prompt or terminal window in the repository directory.
4. Run the script with the command python gmailDotTrickGenerator.py.
5. Enter an email address when prompted and press Enter.
6. Wait for the script to finish generating variants and saving them to a file.
7. Check the file variants.txt in the current directory for the generated variants.

# Notes
The script uses a generator to produce variants one by one, so it can handle large usernames without running out of memory.
The script assumes that the email address is valid and has exactly one "@" symbol separating the username and domain parts.
