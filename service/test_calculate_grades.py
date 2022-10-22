import pytest
from calculateGrades import calculateFinalGrade

def testFinalGrade():
    assert calculateFinalGrade([3,3,3,3]) == 3

def testFinalGrade2():
    assert calculateFinalGrade([3.6,4.8,2.4,3.3]) == 3.53