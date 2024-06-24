# CS499-ePortfolio

## Professional Self-Assesment


## Snr-Project File
This is my original project. It was originally a juptyer notebook which I worked on within an online lab environment for one of my classes. In preparing the project for this class I downloaded it from the lab environment to my own machine and made it a normal python file instead of a jupyter notebook. Within these changes I ran into a lot of issues with preparing the dependencies for the code. Specifically I ran into a lot of issues with getting the right version of TensorFlow which was needed for the algorithm to work. After dead-end followed by dead-end I came to the conclusion that I was not going to be able to fix this problem within the timeline I had.

## Snr-Project-backup File
This backup project is a proof-of-concept project. I went online and found a different maze solver and got that running on my machine. Once that was done I implemented my 3 enhancements into the new project. The enhancements ended up being a little more simple due to the fact that the time spent on implementing them in the new project was heavily restricted. The database and display functions especially, while functional, have a lot of ways I would have liked to improve them if I had more time.

### How to run the project:
1. Make sure all the needed libraries/dependencies are downloaded.
This project uses tensorflow, numpy, matplotlib, json, and sqlite3.
2. Make sure you are in the top level directory of the project which is the file named SnrProject-backup.
3. Run python3 maze-solver.py in the terminal.
This file needs to be run first as it will create the database file that display-results.py will reference.
4. Run python3 display-results.py in the terminal.
This will give a link to a simple html page that displays some data from the past training sessions.
