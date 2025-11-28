import streamlit as st
import rps_core  # your core game logic


# ========= PAGE CONFIG =========
st.set_page_config(
    page_title="RPS R.A.N.D.O.M",
    page_icon="🕹️",
    layout="wide",
)

# ========= GLOBAL CSS =========
st.markdown("""
    <style>
    .main {
        background: radial-gradient(circle at top, #0f172a 0, #020617 45%, #000000 100%);
        color: #e5e7eb;
        font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .title-text {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #fbbf24;
        text-shadow: 0 0 20px rgba(251, 191, 36, 0.6);
        margin-bottom: 0.2rem;
    }
    .subtitle-text {
        text-align: center;
        font-size: 0.95rem;
        color: #9ca3af;
        margin-bottom: 2rem;
    }
    .score-card {
        background: linear-gradient(145deg, #020617, #0b1120);
        border-radius: 18px;
        padding: 18px 20px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.9);
    }
    .score-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #6b7280;
    }
    .score-value {
        font-size: 2.0rem;
        font-weight: 800;
    }
    .score-player { color: #22c55e; }
    .score-computer { color: #ef4444; }
    .score-rounds { color: #38bdf8; }

    .stat-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #9ca3af;
    }
    .stat-value {
        font-size: 1.2rem;
        font-weight: 700;
        color: #e5e7eb;
    }

    .move-card {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(148, 163, 184, 0.35);
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.85);
    }
    .result-banner-win {
        border-radius: 999px;
        padding: 8px 16px;
        background: linear-gradient(90deg, #22c55e, #16a34a);
        color: white;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 12px 30px rgba(34, 197, 94, 0.6);
        margin-bottom: 10px;
    }
    .result-banner-lose {
        border-radius: 999px;
        padding: 8px 16px;
        background: linear-gradient(90deg, #ef4444, #b91c1c);
        color: white;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 12px 30px rgba(239, 68, 68, 0.6);
        margin-bottom: 10px;
    }
    .result-banner-draw {
        border-radius: 999px;
        padding: 8px 16px;
        background: linear-gradient(90deg, #38bdf8, #0ea5e9);
        color: white;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 12px 30px rgba(56, 189, 248, 0.6);
        margin-bottom: 10px;
    }

    div.stButton > button {
        border-radius: 999px;
        height: 3rem;
        padding: 0 1.8rem;
        border: none;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        background: linear-gradient(135deg, #22c55e, #16a34a);
        color: #0f172a;
        box-shadow: 0 12px 30px rgba(34, 197, 94, 0.4);
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #4ade80, #22c55e);
        transform: translateY(-1px);
    }
    </style>
""", unsafe_allow_html=True)

# ========= SESSION STATE INIT =========
if "player_score" not in st.session_state:
    # per current match
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.rounds_played = 0
    st.session_state.best_of = 3
    st.session_state.last_result = None
    st.session_state.last_moves = None
    st.session_state.round_history = []   # list of dicts, current match

    # career stats (across matches)
    st.session_state.total_rounds = 0
    st.session_state.total_wins = 0
    st.session_state.total_losses = 0
    st.session_state.total_draws = 0
    st.session_state.current_streak = 0    # positive = win streak, negative = lose streak
    st.session_state.max_win_streak = 0
    st.session_state.max_lose_streak = 0

    st.session_state.match_history = []    # list of dicts, all finished matches

# ========= TITLE =========
st.markdown('<div class="title-text">RPS R.A.N.D.O.M</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Rock • Paper • Scissors • Pure Chaos Engine</div>', unsafe_allow_html=True)

# ========= LAYOUT =========
left, right = st.columns([1.3, 1])

# ========= LEFT: GAME CONTROLS & BATTLE LOG =========
with left:
    st.markdown("### 🎮 Your Move")

    st.session_state.best_of = st.number_input(
        "Best of (odd only)",
        value=st.session_state.best_of,
        min_value=1,
        step=2,
        help="First to reach (N // 2 + 1) wins the match.",
    )

    player_move = st.radio(
        "Choose your weapon",
        rps_core.MOVES,
        horizontal=True,
    )

    if st.button("Play Round"):
        # Play one round
        computer_move, result = rps_core.play_round(player_move)
        st.session_state.rounds_played += 1
        st.session_state.total_rounds += 1
        st.session_state.last_result = result
        st.session_state.last_moves = (player_move, computer_move)

        # Update scores + career stats + streak
        if result == "win":
            st.session_state.player_score += 1
            st.session_state.total_wins += 1

            if st.session_state.current_streak >= 0:
                st.session_state.current_streak += 1
            else:
                st.session_state.current_streak = 1

            st.session_state.max_win_streak = max(
                st.session_state.max_win_streak,
                st.session_state.current_streak,
            )

        elif result == "lose":
            st.session_state.computer_score += 1
            st.session_state.total_losses += 1

            if st.session_state.current_streak <= 0:
                st.session_state.current_streak -= 1
            else:
                st.session_state.current_streak = -1

            st.session_state.max_lose_streak = min(
                st.session_state.max_lose_streak,
                st.session_state.current_streak,
            )

        else:
            st.session_state.total_draws += 1
            # draw breaks streak
            st.session_state.current_streak = 0

        # Log this round
        st.session_state.round_history.append({
            "round": st.session_state.rounds_played,
            "player_move": player_move,
            "computer_move": computer_move,
            "result": result,
            "player_score": st.session_state.player_score,
            "computer_score": st.session_state.computer_score,
        })

        # Best-of-N logic
        needed_to_win = st.session_state.best_of // 2 + 1

        def _finish_match(match_result: str):
            """Record a finished match and reset per-match state."""
            rps_core.log_match(
                st.session_state.best_of,
                st.session_state.rounds_played,
                st.session_state.player_score,
                st.session_state.computer_score,
                match_result,
            )
            st.session_state.match_history.append({
                "best_of": st.session_state.best_of,
                "rounds": st.session_state.rounds_played,
                "player_score": st.session_state.player_score,
                "computer_score": st.session_state.computer_score,
                "result": match_result,
            })
            # reset match-only state
            st.session_state.player_score = 0
            st.session_state.computer_score = 0
            st.session_state.rounds_played = 0
            st.session_state.last_result = None
            st.session_state.last_moves = None
            st.session_state.round_history = []

        if st.session_state.player_score == needed_to_win:
            st.balloons()
            st.success("🏆 You won the match! 🎊")
            _finish_match("YOU WIN")

        elif st.session_state.computer_score == needed_to_win:
            st.error("💀 Computer wins the match!")
            _finish_match("COMPUTER WINS")

    # ===== Battle Log Card =====
    st.markdown("### 📣 Battle Log")
    st.markdown('<div class="move-card">', unsafe_allow_html=True)

    if st.session_state.last_result:
        result = st.session_state.last_result
        player_move, computer_move = st.session_state.last_moves

        if result == "win":
            st.markdown(
                '<div class="result-banner-win">🎉 You win this round!</div>',
                unsafe_allow_html=True,
            )
        elif result == "lose":
            st.markdown(
                '<div class="result-banner-lose">💀 Computer takes this round!</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="result-banner-draw">🤝 It&apos;s a draw!</div>',
                unsafe_allow_html=True,
            )

        st.markdown(
            f"**You:** `{player_move}`  vs  **Computer:** `{computer_move}`"
        )
    else:
        st.markdown("_Make your first move to start the duel._")

    st.markdown("</div>", unsafe_allow_html=True)

    # ===== Round History Table =====
    st.markdown("### 🧾 Round History")
    if st.session_state.round_history:
        st.dataframe(
            [
                {
                    "Round": r["round"],
                    "You": r["player_move"],
                    "Computer": r["computer_move"],
                    "Result": r["result"].upper(),
                    "Score (You-CPU)": f'{r["player_score"]}-{r["computer_score"]}',
                }
                for r in st.session_state.round_history
            ],
            use_container_width=True,
        )
    else:
        st.caption("No rounds played in this match yet.")

# ========= RIGHT: SCOREBOARD, STATS & MATCH HISTORY =========
with right:
    # --- core scoreboard ---
    st.markdown("### 📊 Scoreboard")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="score-label">Player</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="score-value score-player">{st.session_state.player_score}</div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown('<div class="score-label">Computer</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="score-value score-computer">{st.session_state.computer_score}</div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown('<div class="score-label">Rounds</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="score-value score-rounds">{st.session_state.rounds_played}</div>',
            unsafe_allow_html=True,
        )

    st.markdown(f"**Match Mode:** Best of {st.session_state.best_of}")
    st.markdown("---")

    # --- career stats ---
    total = st.session_state.total_rounds
    win_rate = (st.session_state.total_wins / total * 100) if total > 0 else 0.0

    s1, s2 = st.columns(2)
    with s1:
        st.markdown('<div class="stat-label">Win rate</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="stat-value">{win_rate:.1f}%  '
            f'({st.session_state.total_wins}W / {total}R)</div>',
            unsafe_allow_html=True,
        )
    with s2:
        # longest win streak and longest lose streak (absolute)
        max_win = st.session_state.max_win_streak
        max_lose = abs(st.session_state.max_lose_streak)
        st.markdown(
            '<div class="stat-label">Best streaks</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="stat-value">Win: {max_win}  ·  Lose: {max_lose}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")

    if st.button("🔁 Reset Match"):
        # reset only current match
        st.session_state.player_score = 0
        st.session_state.computer_score = 0
        st.session_state.rounds_played = 0
        st.session_state.last_result = None
        st.session_state.last_moves = None
        st.session_state.round_history = []
        st.info("Scores reset. New match, same legend 😎")

    with st.expander("Advanced reset options"):
        if st.button("🧨 Full reset (stats + history)"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.experimental_rerun()

    st.markdown("### 🏅 Match History")
    if st.session_state.match_history:
        st.dataframe(
            [
                {
                    "Best Of": m["best_of"],
                    "Rounds Played": m["rounds"],
                    "Final Score": f'{m["player_score"]}-{m["computer_score"]}',
                    "Result": m["result"],
                }
                for m in st.session_state.match_history
            ],
            use_container_width=True,
        )
    else:
        st.caption("Finish a match to see your legacy here.")

# ========= PROJECT SUMMARY (BOTTOM) =========
# ========= PROJECT SUMMARY (BOTTOM CENTER) =========
st.markdown("---", unsafe_allow_html=True)

st.markdown(
    """
<div style="
    display: flex;
    justify-content: center;
    margin-top: 10px;
">
  <div style="
      max-width: 720px;
      border-radius: 16px;
      padding: 18px 22px;
      border: 1px solid rgba(148, 163, 184, 0.45);
      background: radial-gradient(circle at top, #020617 0, #020617 40%, #000000 100%);
      box-shadow: 0 18px 40px rgba(15, 23, 42, 0.9);
      font-family: 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  ">
    <div style="text-align: center; font-size: 1.1rem; font-weight: 700; color: #e5e7eb; margin-bottom: 6px;">
      RPS R.A.N.D.O.M · Learning Project
    </div>
    <div style="text-align: center; font-size: 0.85rem; letter-spacing: 0.16em; text-transform: uppercase; color: #9ca3af; margin-bottom: 14px;">
      Python   Random   Control Flow   Program Design
    </div>
    <div style="font-size: 0.95rem; color: #d1d5db; line-height: 1.55;">
      This project was built to turn a simple Rock Paper Scissors game into a complete, replayable experience while practicing real Python skills. The computer selects moves using the random module, the app manages a full best of N match system, and every round is evaluated with clear win, lose or draw outcomes based on standard RPS rules.
    </div>
    <div style="font-size: 0.95rem; color: #d1d5db; line-height: 1.55; margin-top: 10px;">
      Under the hood this app focuses on clean program structure. Core logic lives in a separate module, Streamlit handles the interface, and the match engine tracks scores, series, history and basic statistics. It is designed as a compact playground to practice the random library, conditional logic, control flow, state management, file logging and modular code that can scale into bigger games or analytics projects.
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)
