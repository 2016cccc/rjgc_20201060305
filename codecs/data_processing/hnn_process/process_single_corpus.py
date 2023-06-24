import pickle
from collections import Counter

def load_pickle(filename):
    return pickle.load(open(filename, 'rb'), encoding='iso-8859-1')


def single_list(arr, target):
    return arr.count(target)

#staqc：把语料中的单候选和多候选分隔开
def data_staqc_prpcessing(filepath,save_single_path,save_mutiple_path):
    with open(filepath,'r')as f:
        total_data= eval(f.read())
        f.close()
    qids = []
    for i in range(0, len(total_data)):
        qids.append(total_data[i][0][0])


    result = Counter(qids)

    total_data_single = []
    total_data_multiple = []
    for i in range(0, len(total_data)):
        if(result[total_data[i][0][0]]==1):
            total_data_single.append(total_data[i])

        else:
            total_data_multiple.append(total_data[i])

    f = open(save_single_path, "w")
    f.write(str(total_data_single))
    f.close()

    f = open(save_mutiple_path, "w")
    f.write(str(total_data_multiple))
    f.close()



#把单候选只保留其qid
def single_unlable2lable(path1,path2):
    total_data = load_pickle(path1)
    labels=[]

    for i in range(0,len(total_data)):
        labels.append([total_data[i][0],1])

    total_data_sort = sorted(labels, key=lambda x: (x[0], x[1]))
    f = open(path2, "w")
    f.write(str(total_data_sort))
    f.close()


if __name__ == "__main__":
    
    language_type= 'python'

    staqc_path = '../hnn_process/ulabel_data/' + language_type + '_staqc_qid2index_blocks_unlabeled.txt'
    staqc_sigle_save ='../hnn_process/ulabel_data/staqc/single/' + language_type + '_staqc_single.txt'
    staqc_multiple_save = '../hnn_process/ulabel_data/staqc/multiple/' + language_type + '_staqc_multiple.txt'
    data_staqc_prpcessing(staqc_path,staqc_sigle_save,staqc_multiple_save)
