from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import testReducerePret, testTrecereRezervariPeUnNume, testSumaPreturiPerNume, \
    testPretMaxperClasa, testOrdonareDupaPretDescrescator


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()

    testReducerePret()
    testTrecereRezervariPeUnNume()
    testSumaPreturiPerNume()
    testOrdonareDupaPretDescrescator()
    testPretMaxperClasa()