import sys
import csv

def main():
    if len(sys.argv) != 3:
        print 'Usage: Input_file TTL_file'
        sys.exit(-1)

    csvName = sys.argv[1]
    ttlName = sys.argv[2]

    infile = open(csvName, 'rb')
    outfile = open(ttlName, 'wa')

    # Parse the input
    dict = {}
    id = 0
    for line in infile:
        # Extract string tokens from line
        tokens = line.split()
        color = tokens[0]
        acronym = tokens[1]
        code = tokens[-1]
        #parent = tokens[-2]
        fullname = tokens[2]
        for i in xrange(3, len(tokens)-1):
            fullname += ' ' + tokens[i]

        info = (fullname, acronym)
        dict[id] = info

        id += 1

    for i in xrange(id):
        fullname = dict[i][0]
        acronym = dict[i][1]
        #parent = dict[i][2]

        outfile.write('MMBA:%05d rdf:type owl:Class ;\n\n'%(i))
        outfile.write('                 rdfs:label "%s"@en ;\n\n'%fullname)
        outfile.write('                 nsu:synonym "%s"@en .\n\n\n'%acronym)

        # parent_flag = False
        # for x in xrange(id):
        #     if dict[x][1] == parent:
        #         parent_id = x
        #         parent_flag = True
        #         break
        # if parent_flag == False:
        #     parent_id = ""
        #     outfile.write('                 nsu:synonym "%s"@en .\n\n'%acronym)
        # else:
        #     outfile.write('                 nsu:synonym "%s"@en ;\n\n'%acronym)
        #     outfile.write('                 rdfs:subClassOf [ rdf:type owl:Restriction ; owl:onProperty nsu:part_of ; owl:someValuesFrom MMBA:%05d ] .\n\n\n\n'%parent_id)


    infile.close()

if __name__ == '__main__':
    main()
