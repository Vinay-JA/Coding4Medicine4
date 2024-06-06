import re


def countRestrictionSites(genomesequence, recognitionsequence):
    recognitionpattern = recognitionsequence.replace('N','[ATCG]')       
    matches = re.findall(recognitionpattern,genomesequence)
    return len(matches)

def findrestrictionsites(genomesequence,recognitionsequence):
    recognitionpattern = recognitionsequence.replace('N','[ATCG]')
    pattern = re.compile(recognitionpattern)
    matches = [match.start() for match in re.finditer(pattern,genomesequence)]
    return matches
def findfragmentlengths(genomesequence,recognitionsequence):
    cutsites = findrestrictionsites(genomesequence,recognitionsequence)
    cutsites = sorted(cutsites)
    cutpositions = [0] + cutsites + [len(genomesequence)]
    fragmentlength = [
        cutpositions[i+1] - cutpositions[i] for i in range(len(cutpositions)-1)
    ]
    return fragmentlength
def readsequence(filepath):
    with open(filepath, 'r') as file:
        genomesequence = file.read().replace('\n','')
    return genomesequence
def main():
    filepath = './Text.txt'
    genomesequence = readsequence(filepath)
    recognitionsequence = "GACNNNNNGTC"
    numsites = countRestrictionSites(genomesequence,recognitionsequence)
    numfragments = numsites + 1
    print(f"The enzyme EclHKI will split the genome into {numfragments} parts.")
    fragmentlength = findfragmentlengths(genomesequence,recognitionsequence)
    print(f"Fragment lengths: {fragmentlength}")
if __name__=="__main__":
    main()
