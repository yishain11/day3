class alienDelegation:
    def __init__(self,name,materials,suggestionNum):
        self.name = name
        self.materials = materials
        self.suggestionNum = suggestionNum

    
    def checkSuggestion(self,suggestion):
        return suggestion in self.materials
    

matrialsList = {1:'cdahbfjd',
                2:'fgddsf',
                3:'jcfgh',
                4:'gzfhnsfg',
                5:'gzzgfd',
                6:'fgagfdsh',
                7:'dhsbf',
                8:'jcsfAfgh',
                9:'cZXVDSG',
                10:'afgdgafg',
                11:'gagdfsga',
                12:'agerygs',
                13:'hshhhhg',
                14:'fsaasfds',
                15:'vzzzzfgDFDzzzds',
                16:'vzzzzzDdshbzzds',
                17:'vzzzzGdszzzds',
                18:'DSGdsG',
                19:'vzzzzFGDHAzzzds',
                20:'FDSAGDS'}

def startNegotiation(delegation):
    print('The negotiation with delegation {} starts now'.format(delegation.name))
    suggestions = 0
    while(delegation.suggestionNum > suggestions):
        x = input('Please chose a suggestion from the matrial list:')
        if matrialsList[int(x)] in delegation.materials:
            return 1
        suggestions += 1
        if delegation.suggestionNum >= suggestions:
            print('Try again:')
    return 0



alienDelegation1 = alienDelegation('FirstDelegation',[matrialsList[3], matrialsList[5],matrialsList[6]] , 3)
alienDelegation2 = alienDelegation('SecondDelegation',[matrialsList[8], matrialsList[9],matrialsList[11]] , 2)
alienDelegation3 = alienDelegation('ThirdDelegation',[matrialsList[18], matrialsList[2],matrialsList[20]] , 4)
alienDelegation4 = alienDelegation('FourthDelegation',[matrialsList[13], matrialsList[15],matrialsList[16]] , 7)

delegations = [alienDelegation1,alienDelegation2, alienDelegation3, alienDelegation4]
finalResult = 0
for i in delegations:
    result = startNegotiation(i)
    if result == 1:
        print('{} is convinced'.format(i.name))
    else:
        print('{} is not convinced'.format(i.name))
    finalResult += result
    print('{}% of the alian groups are convinced'.format(finalResult/4))

if finalResult/4 >= 0.7:
    print('You succeed! {}'.format(finalResult))

else:
    print('You failed!')

