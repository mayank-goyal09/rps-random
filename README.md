# 🎮 RPS R.A.N.D.O.M - Rock-Paper-Scissors Game

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rps-random-project1.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)

> **An intelligent Rock-Paper-Scissors game built with Streamlit that showcases Python fundamentals through interactive gameplay and real-time match tracking.**

## 🚀 Live Demo

**Play now:** [RPS R.A.N.D.O.M Live App](https://rps-random-project1.streamlit.app/)

---

## 💡 What Makes This Special?

This isn't just a simple game—it's a complete learning project that demonstrates clean architecture, modular design, and professional development practices. Built with a developer-first approach, it shows how core Python concepts translate into real-world applications while maintaining code quality and scalability.

### ✨ Key Features

- **🤖 Intelligent AI Opponent** - Computer makes random, unpredictable moves using Python's random module
- **🏆 Best-of-N Series** - Play matches with customizable difficulty levels (3, 5, 7, etc.)
- **⚡ Real-time Scoreboard** - Instant feedback with live score updates and match progress
- **📊 Match History Logging** - Complete transaction history with timestamps for future analytics
- **🎨 Modern UI/UX** - Beautiful dark-mode Streamlit interface designed for optimal user experience
- **📱 Responsive Design** - Seamless gameplay across all devices and screen sizes

---

## 🛠️ Technical Architecture

### Built With

- **Frontend & Backend**: Streamlit (Python)
- **Core Logic**: Pure Python with random module
- **Data Storage**: Text file-based match logging
- **State Management**: Streamlit session state
- **Deployment**: Streamlit Cloud

### Project Structure

rps-random/
│
├── app.py # Main Streamlit application & UI
├── rps_core.py # Pure game logic (no UI dependencies)
├── rps_history.txt # Match logs with timestamps
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## 🎯 Core Functionality

### Game Mechanics
- Standard Rock-Paper-Scissors rules with instant win detection
- Draw handling for tied rounds
- Automatic match termination when someone reaches majority wins
- Support for both quitting mid-match and graceful resets

### AI Opponent
- Random move selection using `random.choice()`
- Unpredictable gameplay for authentic challenge
- Fair and unbiased decision-making

### Match Management
- Customizable best-of-N series (odd numbers only)
- Real-time scoreboard with player, computer, and round tracking
- Win rate calculation and streak monitoring
- Early quit option without penalty

---

## 🚦 Getting Started

### Prerequisites

- Python 3.9 or higher
- streamlit

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/mayank-goyal09/rps-random.git
cd rps-random
```

2. **Create virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
streamlit run app.py
```

5. **Access the app**
- Open your browser and navigate to `http://localhost:8501`

---

## 📖 Usage Guide

### Starting a Match
1. Select your preferred difficulty (Best of 3, 5, or 7)
2. Click the "PLAY ROUND" button to begin

### Making Your Move
1. Choose your weapon: Rock, Paper, or Scissors
2. Click "PLAY ROUND" to challenge the computer
3. View instant results and updated scoreboard

### Understanding the Results
- **You Win** ✅ - Your move beats computer's move
- **Computer Wins** 💀 - Computer's move beats yours
- **Draw** 🤝 - Both chose the same move

### Match Completion
- First to reach majority wins the match
- View final score and match summary
- Click "RESET MATCH" to start a fresh game

### Viewing Statistics
- Win rate percentage displayed in real-time
- Best streaks tracked throughout your session
- Battle log shows complete round-by-round history

---

## 💻 Code Architecture

### `rps_core.py` - Pure Game Logic

```python
def play_round(player_move):
    """Execute single round and return winner."""
    computer_move = random.choice(MOVES)
    return computer_move, result

def log_match(best_of, rounds_played, player_score, computer_score, result):
    """Persist match data to file with timestamp."""
    # Appends to rps_history.txt
```

**Key Design Principle**: No Streamlit imports—pure Python logic that's reusable and testable.

### `app.py` - Streamlit Frontend

```python
import rps_core
if st.button("PLAY ROUND"):
    computer_move, result = rps_core.play_round(player_move)
    # Update UI and session state
```

**Key Design Principle**: UI-only code—keeps interface logic separate from game mechanics.

---

## 📊 Sample Match History

Your matches are automatically logged to `rps_history.txt`:

```
2025-11-28 10:45:32, Best of 3, Rounds: 2, You: 2, Computer: 0, Result: YOU WIN
2025-11-28 10:46:15, Best of 5, Rounds: 4, You: 2, Computer: 2, Result: COMPUTER WINS
2025-11-28 10:47:02, Best of 3, Rounds: 3, You: 1, Computer: 2, Result: COMPUTER WINS
```
---

## 🎓 What I Learned

Building this project strengthened my skills in:

- **Python Fundamentals**: Control flow, loops, input validation, and random module usage
- **Modular Design**: Separating concerns between logic and UI for maintainability
- **State Management**: Handling complex application states with Streamlit's session_state
- **File I/O Operations**: Persistent data storage and log management
- **Interactive Development**: Creating responsive user interfaces with Streamlit
- **Version Control**: Professional Git workflows and GitHub repository management
- **Deployment**: Publishing Python applications to cloud platforms

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/mayank-goyal09/rps-random/issues).

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 About the Developer

Built with passion by **Mayank Goyal** - A Python developer and aspiring data professional currently pursuing Class 11th, with hands-on experience in:

- Python Programming & Game Development
- Full-stack Development with Streamlit
- Data Analysis & Visualization
- Interactive Application Development

### 🔗 Connect With Me

- GitHub: [@mayank-goyal09](https://github.com/mayank-goyal09)
- Portfolio: [Coming Soon](#)

---

## ⭐ Show Your Support

If you found this project helpful or interesting, please consider giving it a star! It helps others discover the project and motivates me to build more innovative solutions.

---

## 📧 Contact

Have questions or suggestions? Feel free to reach out!

---

**Made with ❤️ using Streamlit and Python**

*"Building games that teach, interfaces that inspire."*
