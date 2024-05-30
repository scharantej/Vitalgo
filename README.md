## A Game of Life Simulator Using Flask

### HTML Files

**1. index.html (Main Page)**
- HTML template for the main page of the application.
- Contains a canvas element where the game board will be rendered and buttons to control game simulation.

**2. layout.html (Base Template)**
- Shared base template for all other HTML files.
- Includes common HTML elements such as header, navigation, and footer.

### Routes

**1. GET /**
- Main application route that renders the index.html template and initializes the game.

**2. POST /step**
- Route to handle the game's simulation step.
- Receives the current game board state as JSON data and returns the updated state.

**3. POST /reset**
- Route to reset the game board to its initial state.