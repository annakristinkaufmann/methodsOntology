import sys
import csv

def main():
    if len(sys.argv) < 4:
        print 'Usage: CSV_file TTL_file AtlasName'
        sys.exit(-1)

    csvName = sys.argv[1]
    ttlName = sys.argv[2]
    atlasName = sys.argv[3]

    infile = open(csvName, 'rb')
    reader = csv.reader(infile)

    outfile = open(ttlName, 'wa')

    # Load the csv into a matrix

    row_id = 0

    table = []
    for row in reader:
        if row_id == 0:
            header = row
        else:
            table.append(row)
            id = int(row[1])
            label = row[2]
            synonym = row[0]

            outfile.write(atlasName + ':%05d rdf:type owl:Class ;\n\n'%id)
            if label == '-------':
                outfile.write('                 rdfs:label "%s"@en ;\n\n'%synonym)
                outfile.write('### TOFIX: rename the ------- to proper name                 rdfs:label "%s"@en ;\n\n'%label)
            else:
                outfile.write('                 rdfs:label "%s"@en ;\n\n'%label)
                outfile.write('                 nsu:synonym "%s"@en ;\n\n'%synonym)
            if row[3] != '':
                parent = int(row[3])
                outfile.write('                 rdfs:subClassOf [ rdf:type owl:Restriction ; owl:onProperty nsu:part_of ; owl:someValuesFrom '+atlasName+':%05d ] .\n\n\n\n'%parent)

        row_id += 1

    infile.close()

if __name__ == '__main__':
    main()
