'''
Created on 19/01/2015

@authors:     Genessis Sanchez
              Gustavo Gutierrez
'''
import unittest
from Reserva import *
from datetime import MINYEAR
from datetime import MAXYEAR

class TestCalcularPrecio(unittest.TestCase):
        
    # Tests de frontera sobre la entrada  
    # Casos unica tarifa
    def testLimiteInferiorDiariaConNocturna(self):
        self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,6,1),
                                        datetime.datetime(2015,1,19,8,15),
                                        Tarifa(50,60)), 150)




    # Casos unica tarifa tocando las fronteras

    def testFronteraSuperiorDiariaConNocturna(self):
    	self.assertEqual(calcularPrecio(datetime.datetime(2015,1,19,17,0),
    									datetime.datetime(2015,1,19,18,0),
    									Tarifa(50,70)), 50)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()