import os
import json
from matplotlib import pyplot

#対象のファイル及び命名規則を指定
file_text = "amazonaws"

#分割したwordを格納したファイルを指定
corpus_dir = os.path.join("export", f"{file_text}.txt")
#wordと出現回数を格納するファイルを指定
count_result = os.path.join("export", f"{file_text}.json")
#グラフを出力するファイルを指定
graph_result = os.path.join("export", f"{file_text}.png")


#分割したbigramのwordと出現回数を格納
Bigram_dict = {}
#出現回数を対象にソートした成果物を格納
Sorted_dict = {}


#デバッグ用
debug = False


#対象とするコーパスのサンプル数を指定。単位は"行
sample_num = 1000

def main() -> None:
    global Sorted_dict
    global Bigram_dict
    #サンプルカウント
    count = 0

    #0x0000~0xffffまでの文字列をキーとしてBigram_dictに記録
    for i in range(0x0000, 0xffff+1):
        Bigram_dict[f'{i:04x}'] = 0

    with open(corpus_dir, "r") as f:
        #コーパスの中身を1行ずつ読み込む
        for line in f:
            count += 1
            if count == sample_num: break
            #スペースで区切る
            words=line.split()
            #区切った単語を1つずつ取り出す
            for word in words:
                word_counter(word)

    #出現回数を対象にソート
    #dict_sort()


    #出現回数を対象に結果をjsonで出力
    with open(count_result, "w") as f:
        json.dump(Bigram_dict, f, indent=4)
    

    x = list(Bigram_dict.keys())
    y = list(Bigram_dict.values())

    pyplot.figure(figsize=(20,10))
    pyplot.plot(x,y)
    pyplot.title(file_text,fontsize=35)
    pyplot.xlabel("Word",fontsize=25)
    pyplot.ylabel("Frequency",fontsize=25)
    pyplot.xticks(x[::500],rotation=90)
    pyplot.savefig(graph_result,dpi=300)



def word_counter(word) -> None:
    global Bigram_dict    

    #dictに記録する際、大文字に変換して記録
    if debug == True : print(f"word:{word}")
    Bigram_dict[word] += 1



def dict_sort() -> None:
    global Bigram_dict
    global Sorted_dict
    #Bigram_dictを出現回数を対象にソート
    Sorted_dict = dict(sorted(Bigram_dict.items(),key=lambda fruit : fruit[1], reverse=True))
    if debug == True : print(Sorted_dict)



if __name__ == "__main__":
    main()
