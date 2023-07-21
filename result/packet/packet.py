from scapy.all import *
import os

def tcp_ip(directory):
    #TCP/IPの各層を解析

    network = {}
    internet = {}
    transport = {}
    application = {}

    # PCAPファイルの読み込み
    for filename in os.listdir(directory):
        pcap_file = os.path.join(directory, filename)
        if os.path.isfile(pcap_file):
            packets = rdpcap(pcap_file)
            for packet in packets:

                #Layer1の解析
                if network.get(packet[0].name) == None:
                    network[packet[0].name] = 1
                else:
                    network[packet[0].name] += 1
                
                #Layer2の解析
                if internet.get(packet[1].name) == None:
                    internet[packet[1].name] = 1
                else:
                    internet[packet[1].name] += 1

                #Layer3の解析
                if len(packet.layers()) >= 3:
                    if transport.get(packet[2].name) == None:
                        transport[packet[2].name] = 1
                    else:
                        transport[packet[2].name] += 1
                else:
                    if transport.get("NO DATA") == None:
                        transport["NO DATA"] = 1
                    else:
                        transport["NO DATA"] += 1

                #Layer4の解析
                if len(packet.layers()) >= 4:
                    if application.get(packet[3].name) == None:
                        application[packet[3].name] = 1
                    else:
                        application[packet[3].name] += 1
                else:
                    if application.get("NO DATA") == None:
                        application["NO DATA"] = 1
                    else:
                        application["NO DATA"] += 1
        
    return network,internet,transport,application

def main():
    directory = "packet-old/8"
    network,internet,transport,application = tcp_ip(directory)
    print(network)
    print(internet)
    print(transport)
    print(application)
    print("\n")

if __name__ == '__main__':
    main()