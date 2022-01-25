# Contributing
Thank you for contributing to the development of INITATOR_SET, this is a quick guide just to let you know how to navigate this project.

## Project structure 
INITIATOR_SET is divided into submodules, these are;

* Genetic Data Inputs
* eORFs
* Gene names
* UTR & CDS
* Ribosome Profiling predicted genes
* Mutations
* Edits
* Map new AICs
* FASTA
* Protein Targeting & Localisation
* Annotation Matcher
* Functional Comparison Between Predicted Proteins
* Kozak Calculator
* Leaky Scanning Detector
* GC Count
* IRES or hairpin loop predictor
* uORF Proximity
* Ribosomal Assembly Checker

Most of these have yet to be coded, any submodules pending creation will be raised as a milestone, with a corresponding branch raised in the format `feature/[submodule]`.

## Bugs and features

If any bugs are found, general bugs may be raised to [Python issue backlog](https://gitlab.vulpinedesigns.com/TheGUESSUniversalEditingSuiteandSDK/INITIATOR_SET/-/milestones/1#tab-issues) milestone and may be resolved in the `bugs/backlog` branch. If multiple related bugs are found it a be worth raising a milestone and related branch with the format `bugs/[milestone]`. In general;

* Milestone = Branch

Any new features simiarly should also have a milestone raised and a branch with the format `feature/[milestone]`, similarly to the above as all submodules are features. 

When creating a feature try and break it down into component parts (don't get too crazy) and raise a task under that milestone, an example would be;
```
* [Milestone] Fasta submodule 
---- [Task] Parse FASTA file
---- [Task] Generate FASTA file 
```
The aim is to track back any code to the specification in order to make future maintainance easier.

## Code quality 

Once you are ready to merge in your changes, a MR will be raised and we will review and check your code, we're not overtly strict but try and follow these rules;

 * Variable and function names should be distinctive and descriptive; try to avoid too many similarly named values.
 * Functions should be short and snappy, following the advice of [Uncle Bob](https://en.wikipedia.org/wiki/Robert_C._Martin) if a function is above 20 lines, look at refactoring functionality out.
 * Indentation - this is mainly occurs with nested if and for, try and seperate out iteration into other functions or use iteration methods, early returns are your friend;
 ```
 # This!
 def divide(a, b):
	if(b == 0):
		return "Not a number"
	return a / b
	
 # Not this.
 def divide(a, b):
	if(b != 0):
		return a / b
	else:
		return "Not a number"
 ```
 * Seperating your concerns, use multiple source files, don't put everying in a single 1000+ line file, this is very hard to navigate, in general you should look to refactor if your file starts exceeding 250 lines.
