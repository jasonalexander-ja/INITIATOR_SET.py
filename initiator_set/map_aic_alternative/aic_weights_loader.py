from typing import *
from io import StringIO
from dataclasses import *
from initiator_set.map_aic_alternative.map_aic import *


# Interprets an [input file or something] of AIC weights into a collection of AICWeights instances
def interpret_aic_weights(datafile: StringIO, filename: str = "") -> AICDictionary:
    aic_weights: List[AICWeights] = []
    last_line_was_terminated = False
# try:
    while True:
        # I don't claim to know how to read python files
        line = datafile.readline()
        if line is None or line == "":
            if last_line_was_terminated:
                break
            else:
                last_line_was_terminated = True
        line = remove_comments(line)
        line = line.split('\n')[0]
        if line == "":
            continue

        aic_weights.append(interpret_aic_weight(line))
    # except ValueError:
    #     errormsg = "Cannot parse data."
    #     if filename != "":
    #         errormsg += " Misunderstood file " + filename
    #     raise ValueError(errormsg)

    return AICDictionary(aic_weights)


# Interprets a string like "AAA 1" into codon and weight
def interpret_aic_weight(weights: str) -> AICWeights:
    s: List[str] = weights.split()
    if len(s) == 2 and s[0].isalpha():
        return AICWeights(codon=s[0], weight=float(s[1]))
    else:
        raise ValueError("Malformed AIC weights")


# Ignore any comments with the parser
def remove_comments(line: str) -> str:
    return line.split("#")[0]
