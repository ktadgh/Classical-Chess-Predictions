[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
# Chessnet: Predicting chess results and ELO ratings based on PGN data
![Screenshot](https://github.com/ktadgh/Classical-Chess-Predictions/blob/744a6e52eef36ff2d63f2511ab5945c51104f5c3/images/b6.png)

## Classical Project
Using logistic regression to predict the result of a chess game based on the players' ELOs and other factors
The regression model predicts wins, losses and draws, and overall can predict the expected points more accurately
than the ELO alone.

## Neural Network
Using a Recurrent Neural network to predict a player's ELO rating based on Stockfish's evaluation of a single game. 

## Contents
├───Classical Project.ipynb - *Notebook containing the analysis and model*\
├───Database.ipynb - *The functions used to generate csvs from the pgns* \
├───NeuralNet - *Notebook containing the Neural Network*
├───moves_process.py - *Functions to get game performance metrics*\
├───process.py - *Generating csv with performance metrics included*\
├───README.md\
├───csvs\
├───pgns\
├───pgn2data - *I used a slightly edited version of pgn2data*\
├───stockfish_15_win_x64_avx2 - *engine used for the evaluations*



