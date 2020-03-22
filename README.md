# python_task
Python Challenge for JDERobot GSOC 2020

Conway’s Game of Life
The Game of Life is a cellular automaton design by the British mathematician John
Horton Conway in 1970. The target of this challenge is to implement the Game of Life in
python. The application cgol_app.py will be executed from a terminal and it refreshs the grid in
each iteration with information about the game and the evolution of the patterns. When the
application starts the user should choose a pattern to start the game. A json configuration file 
stores all configurable options of game.

To install python dependencies:
```bash
pip3 install -r requirements.txt
```

To clone the package:
```bash
git clone https://github.com/ojitmehta123/python_task.git
```

To use Sample Application:
```bash
cd python_task
python3 cogol_app.py
```

Video Samples:  
[Pulsar](https://drive.google.com/file/d/1ICItxhXeRegn9U069zSGjV4wmvlUumSt/view?usp=sharing)  

[Random Initialization](https://drive.google.com/file/d/1m0vwzXXx9SygDYWt2D7bIC8Cn495UI0_/view?usp=sharing)

All configurations are in config.json in config folder  
To Test run the following from root folder:
```bash
nosetests -sv
```
Output:
```bash
ojit@tyjo:~/temp/task_g/congol$ nosetests -sv
congol.tests.congol_tests.testBlockPeriod ... ok
congol.tests.congol_tests.testTubPeriod ... ok
congol.tests.congol_tests.testToadPeriod ... ok
congol.tests.congol_tests.testBlinkerPeriod ... ok
congol.tests.congol_tests.testPulsarPeriod ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.068s

OK
```
