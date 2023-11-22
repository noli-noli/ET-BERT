import os
from matplotlib import pyplot

corpus_dir = os.path.join("export")

minimal_lines = 0


def main() -> None:
    global minimal_lines
    for root,dirs,files in os.walk(corpus_dir):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root,file), "r") as f:
                    lines = f.readlines()
                    line_count = len(lines)
                    if minimal_lines == 0:
                        minimal_lines = line_count
                    elif minimal_lines > line_count:
                        minimal_lines = line_count
                    print(f"{file} : {line_count}")
    print(f"minimal_lines : {minimal_lines}")
    save_graph()

 
def save_graph() -> None:
    global minimal_lines
    Bigram_dict = {}

    fig, ax = pyplot.subplots(figsize=(20,10))
    pyplot.xticks(rotation=90)

    for root,dirs,files in os.walk(corpus_dir):
        for file in files:
            if file.endswith(".txt"):
                for i in range(0x0000, 0xffff+1):
                    Bigram_dict[f'{i:04x}'] = 0
                count = 0
                with open(os.path.join(root,file), "r") as f:
                    #コーパスの中身を1行ずつ読み込む
                    for line in f:
                        count += 1
                        if count == minimal_lines: break
                        #スペースで区切る
                        words=line.split()
                        #区切った単語を1つずつ取り出す
                        for word in words:
                            Bigram_dict[word] += 1
                    ax.plot(list(Bigram_dict.keys()), list(Bigram_dict.values()), label=file.replace(".txt",""))
    ax.set_title("TLS_Family",fontsize=35)
    ax.set_xlabel("Word",fontsize=25)
    ax.set_ylabel("Frequency",fontsize=25)
    ax.set_xticks(list(Bigram_dict.keys())[::500])
    ax.legend()
    pyplot.savefig(f"TLS_Family.png",dpi=300)

if __name__ == "__main__":
    main()