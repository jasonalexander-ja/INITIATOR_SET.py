from typing import *
from initiator_set.map_aic_alternative.aic_weights_loader import *

print("Test individual weights parsing")
print("CUG 100, " + interpret_aic_weight("CUG 100").__str__())
print("AUG 1000 , " + interpret_aic_weight("AUG 1000 ").__str__())
print("   GUG       11      , " + interpret_aic_weight("   GUG       11      ").__str__())
exceptioned = False
try:
    print("[invalid]   GUG       11      , " + interpret_aic_weight("[invalid]   GUG       11      ").__str__())
    print("   GUG       11    [invalid]  , " + interpret_aic_weight("   GUG       11    [invalid]  ").__str__())
except ValueError:
    exceptioned = True
if not exceptioned:
    print("Did not exception on malformed input")

print("\nTest collective weights parsing")
print("CUG 100|AUG 1000 |   GUG       11      " + interpret_aic_weights(StringIO("CUG 100\nAUG 1000 \n   GUG       11      ")).__str__())

print("\nTest AIC Dict")
asdf = interpret_aic_weights(StringIO("CUG 100\nAUG 1000\nCUG 20"))
print("CUG 100\nAUG 1000\nCUG 200\nGUG 50" + asdf.__str__())

print("\nTest AIC Dict Methods")
print("CUG 100|AUG 1000|CUG 200|GUG 50")
asdf = interpret_aic_weights(StringIO("CUG 100\nAUG 1000\nCUG 200\nGUG 50"))
print(asdf.sorted_by_weights().__str__())

print("\nTest Map AIC")
print("AUG 1000|CUG 200|GUG 50 on CCCAUGAUGCCCGUG")
asdf = map_aic(AICDictionary([('AUG', 1000)]), "CCCAUGAUGCCCGUG")
print(asdf.aics)
print("By closest position: "+asdf.collapse_by_position().__str__())
print("By priority codons: "+asdf.collapse_by_priority({'AUG': 1000, 'CUG': 200, 'GUG': 50}).__str__())

print("\nTest AIC Map Methods")
print("AUG 1000|CUG 200|GUG 50 on CUGAUGGUG")
asdf = AICMap({'CUG': [0], 'AUG': [3], 'GUG': [6]})
print("By closest position: "+asdf.collapse_by_position().__str__())
print("By priority codons: "+asdf.collapse_by_priority({'AUG': 1000, 'CUG': 200, 'GUG': 50}).__str__())

print("\nTest IO")
with (open("example_input.txt")) as inf:
    asdf: AICDictionary = map_aic(interpret_aic_weights(inf), "CUGAUGGUG")
    print(asdf.__str__())
    print("By closest position: "+asdf.collapse_by_position().__str__())
    print("By priority codons: "+asdf.collapse_by_priority({'AUG': 1000, 'CUG': 200, 'GUG': 50}).__str__())
