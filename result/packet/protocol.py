from scapy.all import *

def test(pcap_files):

    # PCAPファイルの読み込み
    packets = rdpcap(pcap_files)
        # パケットの数を表示
    print("Packet count:", len(packets))
    # パケットの情報表示
    for packet in packets:
        print(packet.summary())
    # 結果を表示します
    for proto, count in protocols.items():
        print(f"Protocol {hex(proto)}: {count} packets")


test("2020-06-06_20-25-02.pcap")