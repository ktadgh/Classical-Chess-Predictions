[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
# Chessnet: Predicting chess results and ELO ratings based on PGN data
![Screenshot](https://github.com/ktadgh/Classical-Chess-Predictions/blob/744a6e52eef36ff2d63f2511ab5945c51104f5c3/images/b6.png)

## Blitz Project
Using logistic regression to predict the result of a chess game based on the players' ELO ratings and other factors.
The regression model returns the predicted probability of a win, loss and draw, and overall can predict the expected points more accurately
than the ELO alone.

<p float="left">
<img src=https://github.com/ktadgh/chessnet/blob/main/images/ELO_acc.png width="350" height="300" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src=https://github.com/ktadgh/chessnet/blob/main/images/Model_acc.png width="350" height="300" />
 </p>

## Neural Network
Using a Recurrent Neural network (LSTM) to predict a player's ELO rating based on Stockfish's evaluation of a single game and time spent per move. Results of the model are shown below, compared to a basic linear regression model based on average centipawn loss. The model appears to be outperforming the average centipawn loss model in mean squared error, and also predicts a wider range of values. 

<p float="left">
<img src=https://github.com/ktadgh/chessnet/blob/main/images/NN_linreg_acc1.png width="350" height="300" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src=https://github.com/ktadgh/chessnet/blob/main/images/NN_model_acc1.png width="350" height="300" />
 </p>


## Contents
├───Blitz Project.ipynb - *Notebook containing the analysis and model*\
├───Database.ipynb - *The functions used to generate csvs from the pgns* \
├───NeuralNet - *Notebook containing the Neural Network* \
├───moves_process.py - *Functions to get game performance metrics*\
├───images - contains the graphs included above\
├───README.md\
├───csvs\
├───pgns\
├───stockfish_15_win_x64_avx2 - *engine used for the evaluations*



