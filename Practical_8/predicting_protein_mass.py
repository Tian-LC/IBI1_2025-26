def PPM (t):
    amino = {'G':57.02, 'A':71.04, 'S':87.03, 'P':97.05, 'V':99.07, 'T': 101.05, 'C':103.01, 'I':113.08, 'L':113.08, 'N':114.04, 'D':115.03, 'Q': 128.06, 'K':128.09, 'E':129.04, 'M':131.04, 'H':137.06, 'F':147.07, 'R':156.10, 'Y':163.06, 'W':186.08}
    mass = 0
    for i in t:
        if i in amino:
            mass += amino[i]
        else:
            return "ERROR: at least one aminos are not be defined"  ## it(-1) means an error
    return round(mass,2)

###calling example###
target = "GGGFAA"
print("the example sequence is GGGFAA")
print("the prediction mass of example sequence is", PPM(target),"\n")
#input: GGGFAA(any protein sequence)
#output: 460.21(predicted mass of the protein sequence)

###using example###
target = input('Please input the target protein sequence: ')
print(PPM(target))



