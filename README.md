# Classical Chess Predictions
![Screenshot](https://raw.githubusercontent.com/ktadgh/Classical-Chess-Predictions/blob/main/bin1.png)
Using logistic regression to predict the result of a chess game based on the players' ELOs and other factors
The regression model predicts wins, losses and draws, and overall can predict the expected points more accurately
than the ELO alone.
## Contents
├───Classical Project.ipynb - *Notebook containing the analysis and model*\
├───Database.ipynb - *The function used to generate the csv from the pgns* \
├───moves_process.py - *Functions to get game performance metrics*\
├───process.py - *Generating csv with performance metrics included*\
├───README.md\
├───csvs\
├───pgns\
├───pgn2data - *I used a slightly edited version of pgn2data*\
├───stockfish_15_win_x64_avx2 - *engine used for the evaluations*

## Future work
Next, I want to use the pgn2data package and stockfish to analyze games and see how centipawn loss, number of blunders and 
other game data can predict the game winner, and assessing whether there are trends in performance metrics like these.
