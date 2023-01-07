# game-project
project for game

### Directory Structure
- `src/` contains all game code files
- `assets/` contains all assets for the game
- `tests/` contains all test files

### Running the project
`python run.py`
### Install the dependencies 
`pip install -r requirements.txt`

### Building the executable
The project is compiled using pyinstaller. You can compile the project using the following command:

`pyinstaller run.spec`

You can then find the exe binary in the `dist` folder.

### Running Tests
Tests can be run using the following command: 

`pytest tests`