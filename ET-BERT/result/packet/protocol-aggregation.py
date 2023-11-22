from scapy.all import *
from pathlib import Path

def protocol(pcap_file):

    network = {}
    internet = {}
    transport = {}
    application = {}

    # PCAPファイルの読み込み
    packets = rdpcap(pcap_file)
    #print("Packet count:", len(packets))
    # パケットの情報表示
    for packet in packets:


        if network.get(packet[0].name) == None:
            network[packet[0].name] = 1
        else:
            network[packet[0].name] += 1
        

        if internet.get(packet[1].name) == None:
            internet[packet[1].name] = 1
        else:
            internet[packet[1].name] += 1


        if len(packet.transports()) >= 3:
            if transport.get(packet[2].name) == None:
                transport[packet[2].name] = 1
            else:
                transport[packet[2].name] += 1
        else:
            if transport.get("NO DATA") == None:
                transport["NO DATA"] = 1
            else:
                transport["NO DATA"] += 1


        if len(packet.transports()) >= 4:
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
    network,internet,transport,application = protocol(target)
    print(network,internet,transport,application)

target="2020-06-06_20-25-02.pcap"

if __name__ == '__main__':
    main()