import sys
import csv

def main():
    if len(sys.argv) < 4:
        print 'Usage: file1 file2 diff'
        sys.exit(-1)

    file1_name = sys.argv[1]
    file2_name = sys.argv[2]
    diff_name = sys.argv[3]


    file1 = csv.reader(open(file1_name, 'rb'))
    file2 = csv.reader(open(file2_name, 'rb'))
    diff_file = open(diff_name, 'wa')

    id_1 = []
    id_2 = []
    for row_1 in file1:
        id_1.append(row_1[0])
    for row_2 in file2:
        id_2.append(row_2[0])


    # check common ids and ids in file1 but not in file 2
    comm_id = []
    diff_id_1 = []
    for id in id_1:
        if id in id_2:
            comm_id.append(id)
        else:
            diff_id_1.append(id)

    # check ids in file2 but not in file 1
    diff_id_2 = []
    for id in id_2:
        if id not in id_1:
            diff_id_2.append(id)

    print (comm_id)
    print diff_id_1
    print diff_id_2


if __name__ == '__main__':
    main()