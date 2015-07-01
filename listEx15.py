def applyRules(lhch):
    rhstr = ""
    if lhch == 'H':
        rhstr = 'HFX[+H][-H]'   # Rule 1
    elif lhch == 'X':
        rhstr = 'X[-FFF][+FFF]FX'  # Rule 2
    else:
        rhstr = lhch    # no rules apply so keep the character

    return rhstr


def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr


def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

print(createLSystem(4, "A"))

#So I started off with the template from the lesson that explains L-systems.
#And I replace the A and B changes with the changes for the new l-system
#I need to create.