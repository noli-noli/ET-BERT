import re
import sys

def filter(input,output):
    list = []
    with open(input, 'r') as f:
        tmp = f.readlines()
        list = [line.strip().split('\t')[0] for line in tmp]
    with open(output, 'w') as output_file:
        for element in list:
            output_file.write(f"{element}\n")

def tally(correct_answer,answer):

    with open(correct_answer, 'r') as f:
        correct_answer = f.readlines()
    with open(answer, 'r') as f:
        answer = f.readlines()
    
    true ,false =0,0

    if len(correct_answer) == len(answer):
        length = len(correct_answer)
        for i in range(length):
            if correct_answer[i] == answer[i]:
                true +=1
            else:
                false +=1
    
    print("総要素数:",length,"\n正解数:",true,"\n不正解数:",false,"\n正解率:",true/length*100,"%")

filter('test_dataset.tsv','output.tsv')
tally('prediction.tsv','output.tsv')