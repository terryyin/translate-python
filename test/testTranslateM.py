import unittest
from subprocess import check_output
from os import system, remove

def readFile(s):
    return [i.strip() for i in open(s)]

class TranslateMTest(unittest.TestCase):
            
    def setUp(self):
        self.f_in = "TranslateMTestIn.tFile"
        self.f_out = "TranslateMTestOut.tFile"
        self.f_tmp = "TranslateMTestTmp.tFile"
        
    def test_commandline_input_file_output_std(self):
        result = check_output(["translate", "-i", self.f_in, " "])
        result = result.split("\n")
        result.remove("")
        self.assertEqual(result, readFile(self.f_out))
    
    def test_commandline_input_file_output_file(self):
        cmd = ["translate", "-i", self.f_in, "-o", self.f_tmp, "h"]
        system(" ".join(cmd))
        self.assertEqual(readFile(self.f_tmp), readFile(self.f_out))
        remove(self.f_tmp)

    def test_commandline_input_std_output_file(self):
        cmd = ["translate", "-o", self.f_tmp, "hello"]
        system(" ".join(cmd))
        self.assertEqual(['bonjour'], readFile(self.f_tmp))
        remove(self.f_tmp)

