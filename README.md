# Three-Body Problem Simulation

## Introduction
This project is a simple simulation of the Three-Body Problem, implemented in Python without using external libraries. The Three-Body Problem is a classic problem in physics that involves predicting the motion of three celestial bodies under their mutual gravitational attraction.

## Features
- Simulates the movement of three bodies in a two-dimensional space.
- Uses Newton's laws of motion and universal gravitation.
- Computes the gravitational forces iteratively.
- Basic text-based output of positions.

## How It Works
1. **Initialization**: Define the initial positions, velocities, and masses of the three bodies.
2. **Force Calculation**: Compute the gravitational force on each body due to the other two.
3. **Motion Update**: Update the positions and velocities of the bodies using numerical integration.
4. **Iteration**: Repeat the above steps for a defined number of time steps.

## Project Structure
- `main.py`: The entry point of the simulation.
- `vector.py`: Defines vector operations such as addition, subtraction, and scalar multiplication.
- `body.py`: Represents a celestial body, including attributes like mass, position, and velocity.
- `system.py`: Handles the interactions and computations of the three-body system.

## Usage
### Running the Simulation
1. Clone this repository or download the script.
2. Run the script using Python:
   ```bash
   python main.py
   ```
3. The output will display the updated positions of the three bodies at each time step.

### Customization
- You can modify the initial conditions (positions, velocities, and masses) in the script to observe different behaviors.
- Adjust the time step (`dt`) for accuracy vs. performance trade-offs.

## Example Output
```
Time Step: 1
Body 1 Position: (x1, y1)
Body 2 Position: (x2, y2)
Body 3 Position: (x3, y3)
...
```

## Future Improvements
- Implement energy conservation checks.
- Add a visualization module.
- Use more accurate numerical integration methods.

## License
This project is released under the MIT License.

## Author
Sanyam Rajput

