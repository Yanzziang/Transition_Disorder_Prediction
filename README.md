## Protein Transition Sites and Disorder Regions Prediction

We combined two similar task, protein transition sites prediction and disorder regions prediction, and developed several predictors attempt to identify such regions based on sequence information to promote protein function understanding and drug discovery. Res-BiLstm, which utilizes deep stacking BiLstm layers with shortcut connections, is used for Disorder regions prediction. Res-BiLstm-NN, which performs a transfer of learned disorder knowledge based on Res-BiLstm, is used for transition sites identification. The model of three state classification which can output the probabilities of transitions, non-transition order and disorder is available soon.


## Installation

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
  3. Result written to a ".rb" file in `./Disorder/outcome/`.
  
- Transition prediction by Res-BiLstm-NN
  1. `cd Transition/scripts/`.
  2. `./pred.py <your sequence>.fasta`.
  3. Result written to a ".rbn" file is shown in `./Transition/outcome/`.



**2. Examples**

- Examples of model outcomes are presented in `./Disorder/ex/` and `./Transition/ex/`, respectively.



**3. Features**

- yielded pssm file is in `./features_generation/pssm/`.
- yielded structural features file is in `./features_generation/SPIDER2/ss_file/`.
- yielded physicochemical features file is in `./features_generation/physicochemical/phy_file`.


**4. Usage**

The generation of structural features is on the basis of articles below.
1. R. Heffernan, K. Paliwal, J. Lyons, A. Dehzangi, A. Sharma, J. Wang, A. Sattar, Y. Yang* and Y. Zhou*. Improving prediction of secondary structure, local backbone angles, and solvent accessible surface area of proteins by iterative deep learning. Scientific Reports 2015(5) 
2. R. Heffernan, K. Paliwal, J. Lyons, A. Dehzangi, A. Sharma, J. Wang, A. Sattar, Y. Zhou* and Y Yang*. Highly accurate sequence-based prediction of half-sphere exposures of amino acid residues in proteins. Bioinformatics 2016. 15;32(6):843-9.


### Example: 2019-nCoV (Surface glycoprotein (S))

We particularly provide the transition and disorder prediction results of surface glycoprotein of 2019-nCoV for further promoting drug discovery.
