from typing import *
from io import StringIO


def interpret_aic_weights(datafile: StringIO, filename: str = "") -> Dict[str, float]:
    aic_weights: Dict[str, float] = {}
    last_line_was_terminated = False
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

        entry = interpret_aic_weight(line)
        aic_weights[entry[0]] = entry[1]

    return aic_weights


def interpret_aic_weight(weights: str) -> Tuple[str, float]:
    s: List[str] = weights.split()
    if len(s) == 2 and s[0].isalpha():
        return s[0], float(s[1])
    else:
        raise ValueError("Malformed AIC weights")


# Ignore any comments with the parser
def remove_comments(line: str) -> str:
    return line.split("#")[0]
