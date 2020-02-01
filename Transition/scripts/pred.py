#!/usr/bin/python3

from tensorflow.keras import backend as K
import tensorflow as tf
from tensorflow.keras.backend import set_session
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.visible_device_list = "0"
K=set_session(tf.Session(config=config))

from tensorflow import keras
from tensorflow.keras import *
import pandas as pd
import numpy as np
from sklearn.metrics import auc, roc_curve
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.layers import LSTM, Embedding, Bidirectional, GRU, TimeDistributed, CuDNNLSTM
from tensorflow.keras.models import load_model
from tensorflow.keras.backend import clear_session
import sys, os
import os, sys
import math
import subprocess
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)



def physicochemical(xdir, sequence):
    pdir = xdir + '/../../features_generation/physicochemical'
    subprocess.call(('{0}/phsicochemical.py'.format(pdir), '{0}'.format(sequence)))
    return


def secondary(xdir, sequence):
    sequence_name = os.path.basename(sequence).split('.')[0]
    
    sdir = xdir + '/../../features_generation/SPIDER2/scripts'
    subprocess.call(('{0}/run_local.sh'.format(sdir), '{0}'.format(sequence)))
    
    hsedir = xdir + '/../../features_generation/SPIDER2/HSE'
    spd3file = xdir + '/../../features_generation/SPIDER2/ss_file/{0}.spd3'.format(sequence_name)
    subprocess.call(('{0}/run1.sh'.format(hsedir), spd3file))
    return


def combine(xdir, sequence):
    sequence_name = os.path.basename(sequence).split('.')[0]

    #pssm file list formula
    pssm_dir = xdir + '/../../features_generation/pssm'
    pssm_file = pssm_dir + '/' + sequence_name + '.pssm'
    pssm_tmp = open(pssm_file, 'r')
    pssm_tmp_lst = pssm_tmp.read().splitlines()[3:-6]
    pssm_tmp.close()

    #phy file list formula
    phy_dir = xdir + '/../../features_generation/physicochemical/phy_file'
    phy_file = phy_dir + '/' + sequence_name + '.fasta'
    phy_tmp = open(phy_file, 'r')
    phy_tmp_lst = phy_tmp.read().split('\n')
    phy_tmp.close()
    phy_tmp_lst.remove('')
    phy_tmp_lst = [ele.split('\t')[1:] for ele in phy_tmp_lst]

    #ss file list formula
    ss_dir = xdir + '/../../features_generation/SPIDER2/ss_file'
    spd3file = ss_dir + '/' + sequence_name + '.spd3'
    hsa2file = ss_dir + '/' + sequence_name + '.hsa2'
    hsb2file = ss_dir + '/' + sequence_name + '.hsb2'
    with open(spd3file, 'r') as spd_file, open(hsa2file, 'r') as hsa_file, open(hsb2file, 'r') as hsb_file:
        ss_hse_tmp_lst = []
        for ss_line, hsa_line, hsb_line in zip(spd_file, hsa_file, hsb_file):
            if ss_line.startswith("#") or hsa_line.startswith("#") or hsb_line.startswith("#"): pass
            else:
                hsa_line = [float(i) for i in hsa_line.split()[2:]]
                hsb_line = [float(i) for i in hsb_line.split()[3:]]
                tmp_ss_lst = [float(i) for i in ss_line.split('\n')[0].split('\t')[3:4]] + [float(i) for i in ss_line.split('\n')[0].split('\t')[8:]]
                for ele in ss_line.split('\n')[0].split('\t')[4:8]:
                    ele = float(ele)
                    tmp_ss_lst.append(round(math.sin(ele), 2))
                    tmp_ss_lst.append(round(math.cos(ele), 2))
                tmp = tmp_ss_lst + hsa_line + hsb_line
                ss_hse_tmp_lst.append(tmp)
                
    #combine all files
    len_pssm, len_phy, len_ss = len(pssm_tmp_lst), len(phy_tmp_lst), len(ss_hse_tmp_lst)
    if len_pssm != len_phy != len_ss:
        print(sequence_name + ' rows number are wrong')
    
    pssm_phy_ss = []
    for pssm_line, phy_line, ss_line in zip(pssm_tmp_lst, phy_tmp_lst, ss_hse_tmp_lst):
        pssm_line, phy_line, ss_line = pssm_line.split()[:22], phy_line, ss_line
        pssm_line = [int(pssm_line[i]) if i > 1 else pssm_line[i] for i in range(len(pssm_line))]
        phy_line = [float(ele) for ele in phy_line]
        pssm_phy_ss.append(pssm_line + phy_line + ss_line)
    
    df = pd.DataFrame(pssm_phy_ss)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    #df.to_csv("/usr/Desktop/Protein_Transitions_Disorder_prediction/tmp.csv")
    return df


def prediction(xdir, df):
    x = []
    df = df[df.columns[1:]]
    x.append(df.values.tolist())
    
    model_file = xdir + "/../../models/Res-BiLstm-NN.h5"
    model = load_model(model_file)
    pred = model.predict(np.array(x), batch_size=1)
    pred = pred.tolist()
    pred = [j[0] for i in pred for j in i]

    return pred


def main():
    xdir = sys.argv[0]
    xdir = os.path.abspath(xdir)
    xdir = os.path.dirname(xdir)
    sequence = sys.argv[1]
    sequence = os.path.abspath(sequence)

    physicochemical(xdir, sequence)
    secondary(xdir, sequence)
    df = combine(xdir, sequence)
    result = prediction(xdir, df)
    label = ['T' if ele >= 0.5 else 'N' for ele in result]
    result = ['%.4f' % ele for ele in result]
    
    with open(sequence, 'r') as file:
        residues = file.read().split('\n')
    residues = [ele for ele in residues if ele != '']
    sequence_id = ''
    if len(residues) > 1: sequence_id = residues[0]; sequence_residues = residues[1]
    else: sequence_residues = residues[0]
    if len(result) != len(sequence_residues): print("number of residues and results are not alignment"); sys.exit(1)
    outcome = 'Num' + '\t' + 'AA' + '\t' + 'Proba' + '\t' + 'Label' + '\n'
    for i in range(len(result)):
        outcome += str(i+1) + '\t' + sequence_residues[i] + '\t' + result[i] + '\t' + label[i] + '\n'

    sequence_name = os.path.basename(sequence).split('.')[0] 
    outfile = xdir + '/../outcome/{0}.rbn'.format(sequence_name)
    with open(outfile, 'w') as file:
        title = 'Transition prediction by Res-BiLstm-NN for {0}'.format(sequence) + '\n'
        if sequence_id: outcome = title + sequence_id + '\n' + outcome
        else: outcome = title + outcome
        file.write(outcome)

    return


if __name__ == '__main__':
    main()
