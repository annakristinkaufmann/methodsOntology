import json
import sys

children_name = 'children'
delete_names = ['atlas_id', 'ontology_id', 'color_hex_triplet', 'graph_order', 'st_level', 'hemisphere_id', 'parent_structure_id']


def parse_json(node):
    if node:
        if len(node['children']) == 0:
            del node['children']
        for k in node.keys():
            if k in delete_names:
                del node[k]

    if children_name in node:
        for child in node[children_name]:
            parse_json(child)


def main():
    if len(sys.argv) < 3:
        print('Usage: inputFile outputFile')
        exit(-1)

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    input_file = open(input_name, 'r')
    output_file = open(output_name, 'wa')

    root = json.load(input_file)
    parse_json(root)
    json.dump(root, output_file, sort_keys=False, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    main()
