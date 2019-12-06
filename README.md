# project-fa19
CS 170 Fall 2019 Project
Gradescope doesn't maintain out directory structure and this 
might break our code in certain places
Please place the inputs in /phase_1_inputs/inputs/

and also the mstformater should be inside a directory call mst-solver
that should solve directory issues

We have several ways to run the code
you can just run "python driver_all.py"
This will go through each input in /phase_1_inputs/inputs/
and run driver.py on it 

of you can run each team input one at a time by 
if you run "python driver.py 30_50"

either way driver.py will automatically update the /outputs file with the outputs
properly named for each input

there is another way using bashscripting using driver (executable)
which does the same thing
"driver -f 30_50"