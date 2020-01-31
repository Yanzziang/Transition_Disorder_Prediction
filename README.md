## Transition_Disorder_Prediction

We combined two similar task, protein transition sites prediction and disorder regions prediction, and developed several predictors attempt to identify such regions based on sequence information to promote protein function understanding and drug discovery. Res-BiLstm, which utilizes deep stacking BiLstm layers with shortcut connections, is used for Disorder regions prediction. Res-BiLstm-NN, which performs a transfer of learned disorder knowledge based on Res-BiLstm, is used for transition sites identification. The model of three state classification which can output the probabilities of transitions, non-transition order and disorder is available soon.


## Installation
D
**1. Tool Requirements**
- Keras 2.2.4-tf
- Tensorflow-gpu 1.13.1
- GPUs
- CUDA 9.0/10.0
- Python3, Python2, Pandas

**2. Feature Requirements**
- Uniref or NR dataset
  - If you already had pssm file, you can move pssm file to `./features_generation/pssm/`.
  - If you need make a pssm file, you need download the Uniref or NR dataset and revise the path in the variable "NR" in `./features_generation/SPIDER2/scripts/run_local.sh`.
- Psiblast 
  - Path setting is in `./features_generation/SPIDER2/scripts/run_local.sh`


## Implementation

**1. Running**

- Disorder prediction by Res-BiLstm
  1. `cd Disorder/scripts/`.
  2. `./pred.py <your sequence>.fasta`.
  3. Result is shown in `./Disorder/outcome/`.
- Transition prediction by Res-BiLstm-NN
  1. `cd Transition/scripts/`.
  2. `./pred.py <your sequence>.fasta`.
  3. Result is shown in `./Transition/outcome/`.


**2. Examples**

Examples of model outcomes are presented in `./Disorder/ex/` and `./Transition/ex/`, respectively.


**3. Features**

- yielded pssm file is in `./features_generation/pssm/`.
- yielded structural features file is in `./features_generation/SPIDER2/ss_file/`.
- yielded physicochemical features file is in `./features_generation/physicochemical/phy_file`.




