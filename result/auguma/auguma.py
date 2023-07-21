import csv
import os

target="ek/"
metadata="ek/ek.metadata.tsv"

def classification(pcap,name):
    try:
        if not os.path.exists(name):
            os.makedirs(name)
        os.replace(pcap,name + "/" + pcap.replace("pcap:","").replace("ek/samples/",""))
    except Exception as e:
        print(e)

def tsvreader():
    with open(metadata, newline='') as f:
        for row in csv.reader(f, delimiter='\t'):
            classification(row[2].replace("pcap:",""),row[3].replace("name:","").replace(" ","_"))
