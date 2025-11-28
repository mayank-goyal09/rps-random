# RPS R.A.N.D.O.M
A Rock Paper Scissors Game built with Python and Streamlit

## Live Demo
https://rps-random-project1.streamlit.app/

## What is This?
A simple yet engaging Rock Paper Scissors game where you play against the computer. The game keeps track of your wins, losses, and draws across multiple matches.

## Features
- Play best of N series matches
- Computer opponent using random selection
- Score tracking and match history
- Interactive web interface with Streamlit
- Command line version available

## What I Learned

Building this project taught me several valuable lessons about writing clean code and creating better software:

### Python Fundamentals
- Using the random library to create unpredictable computer moves
- Working with conditional logic and loops for game control
- Validating user input to ensure accurate gameplay

### Software Architecture
- Organizing code into separate modules and functions
- Keeping game logic separate from user interface
- Building reusable components that can grow with the project

### Data Management
- Storing match history in files for persistence
- Managing scores across multiple game sessions
- Logging events systematically

### User Experience
- Creating clear menu options for user navigation
- Providing immediate feedback on game outcomes
- Designing intuitive interfaces that guide users

### Deployment
- Taking a local Python project and deploying it on Streamlit Cloud
- Understanding how web applications serve users
- Managing dependencies and environment setup

## How to Use

### Web Version (Recommended)
Visit: https://rps-random-project1.streamlit.app/

### Local Version
```bash
git clone https://github.com/mayank-goyal09/rps-random.git
cd rps-random
python py_random.py
```

## Project Structure
```
rps-random/
  py_random.py          - CLI game version
  rps_core.py           - Core game logic
  rps_dashboard.py      - Streamlit web app
  match_history.log     - Game records
```

## Technologies Used
- Python 3.8+
- Streamlit (web interface)
- File I/O (for storing game history)

## Why This Project Matters

This project demonstrates that great software comes from understanding the fundamentals well. Rather than building something overly complex, I focused on building something that works reliably and feels good to use.

When recruiters look at projects like this, they see someone who values clarity and good design over unnecessary complexity. These are the qualities that make developers truly valuable to teams.

---

Built with care and attention to detail.
