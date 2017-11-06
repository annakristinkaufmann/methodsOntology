import json
import sys

children_name = 'children'
id_name = 'id'

def write_header(node, outfile):
    if node:
        line = ''
        for key in node.keys():
            line = line + str(key) + ','
        outfile.write(line + '\n')

def parse_json(node, outfile, parent_node):
    if node:
        line = ''
        for key in node.keys():
            if key != children_name:
                line = line + str(node[key]) + ','
        if parent_node == None:
            outfile.write(line + ',\n')
        else:
            outfile.write(line + str(parent_node[id_name]) + '\n')
    if children_name in node:
        for child in node[children_name]:
            parse_json(child, outfile, node)


def main():
    if len(sys.argv) < 3:
        print('Usage: JSONfile CSVfile')
        exit(-1)

    jsonFilename = sys.argv[1]
    ttlFilename = sys.argv[2]

    jsonFile = open(jsonFilename, 'r')
    ttlFile = open(ttlFilename, 'wa')

    root = json.load(jsonFile)
    write_header(root, ttlFile)
    parse_json(root, ttlFile, None)
    ttlFile.close()



if __name__ == '__main__':
    main()