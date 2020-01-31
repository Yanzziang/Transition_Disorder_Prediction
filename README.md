## Transition_Disorder_Prediction

We combined two similar task, protein transition sites prediction and disorder regions prediction, and developed several predictors attempt to identify such regions based on sequence information to promote protein function understanding and drug discovery. Res-BiLstm, which utilizes deep stacking BiLstm layers with shortcut connections, is used for Disorder regions prediction. Res-BiLstm-NN, which performs a transfer of learned disorder knowledge based on Res-BiLstm, is used for transition sites identification. The model of three state classification which can output the probabilities of transitions, non-transition order and disorder is available soon.


## Installation
**Requirement**
- Keras 2.2.4-tf
- Tensorflow-gpu 1.13.1
- GPU
- CUDA 9.0/10.0
- Python3, Python2
- Pandas
