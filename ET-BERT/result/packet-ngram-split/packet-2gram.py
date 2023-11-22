import scapy
import os
import binascii
import argparse
import scapy.all as scapy
from flowcontainer.extractor import extract

packet_path_name = "test"

#対象packetディレクトリ
packet_path = os.path.join("packet",packet_path_name)


#2-gramのファイル名
word_dir= os.path.join("export",packet_path_name)
#パケット毎に改行コードを入れて区切る
payload_1 = os.path.join("export","packet-1.txt")
#パケット全てを1つの纏めとして扱う
payload_2 = os.path.join("export","packet-2.txt")



def main() -> None:
    global packet_path_name
    global packet_path
    global word_dir

    parser = argparse.ArgumentParser(description="--path の後にパケットが格納されているディレクトリを指定せよ")
    parser.add_argument("--path",type=str,default='default_value',help="packet path")
    packet_path_name = parser.parse_args().path
    packet_path = os.path.join("packet",packet_path_name+".txt")
    word_dir= os.path.join("export",packet_path_name+".txt")
    count = 0
    for root,dirs,files in os.walk(packet_path):
        for file in files:
            get_burst_feature(os.path.join(root,file), 64)

def get_burst_feature(label_pcap, payload_len) -> None:
    feature_data = []
    
    packets = scapy.rdpcap(label_pcap)
    
    packet_direction = []
    feature_result = extract(label_pcap)
    for key in feature_result.keys():
        value = feature_result[key]
        packet_direction = [x // abs(x) for x in value.ip_lengths]

    if len(packet_direction) == len(packets):
        
        burst_data_string = ''
        
        burst_txt = ''

        test_txt = ''
        
        for packet_index in range(len(packets)):
            packet_data = packets[packet_index].copy()
            data = (binascii.hexlify(bytes(packet_data)))
            
            packet_string = data.decode()[:2*payload_len]

            ###オリジナルコード###
            #with open(payload_1,'w') as f:
            #    f.write(packet_string + "\n")
            test_txt += packet_string
            #####################
            
            if packet_index == 0:
                burst_data_string += packet_string
            else:
                if packet_direction[packet_index] != packet_direction[packet_index - 1]:
                    
                    length = len(burst_data_string)
                    for string_txt in cut(burst_data_string, int(length / 2)):
                        burst_txt += bigram_generation(string_txt, packet_len=len(string_txt))
                        burst_txt += '\n'
                    #burst_txt += '\n'
                    
                    burst_data_string = ''
                
                burst_data_string += packet_string
                if packet_index == len(packets) - 1:
                    
                    length = len(burst_data_string)
                    for string_txt in cut(burst_data_string, int(length / 2)):
                        burst_txt += bigram_generation(string_txt, packet_len=len(string_txt))
                        burst_txt += '\n'
                    #burst_txt += '\n'
        
        with open(word_dir,"a") as f:
            f.write(burst_txt)
        #以下のコメントアウトを外すと出力される
        #with open(payload_2,'w') as f:
        #    f.write(test_txt)

    return 0



def bigram_generation(packet_datagram, packet_len = 64, flag=True) -> str:
    result = ''
    generated_datagram = cut(packet_datagram,1)
    token_count = 0
    for sub_string_index in range(len(generated_datagram)):
        if sub_string_index != (len(generated_datagram) - 1):
            token_count += 1
            if token_count > packet_len:
                break
            else:
                merge_word_bigram = generated_datagram[sub_string_index] + generated_datagram[sub_string_index + 1]
        else:
            break
        result += merge_word_bigram
        result += ' '
    
    return result



def cut(obj, sec) -> str:
    result = [obj[i:i+sec] for i in range(0,len(obj),sec)]
    try:
        remanent_count = len(result[0])%4
    except Exception as e:
        remanent_count = 0
        print("cut datagram error!")
    if remanent_count == 0:
        pass
    else:
        result = [obj[i:i+sec+remanent_count] for i in range(0,len(obj),sec+remanent_count)]
    return result



if __name__ == '__main__':
    main()
