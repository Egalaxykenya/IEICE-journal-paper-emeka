# Journal Case Study Guide
This short guide highlights the resource structure of the different case study project source files folder. The repository contains 7 folders i.e:
* api_resource_graph_script
* AST
* case_study_sources (Primarily not part of the journal paper)
* DDD-and-Ecore
* RAML
* SOFL
* Threat-Modelling

## api_resource_graph_script
Contains a python implementation of our API resource graph generation and RESTful API url resource list. Your environment should have:
* _Python 3.8_ installed
* _networkx version 2.8.4_ library installed
* _matplotlib version 3.5.2_ library installed
* _matplotlib-inline version 0.1.3_ library installed

To run the graph generation script, execute the python script in your terminal:
```
python salongraph.py 
```
## AST
Contains RAML Abstract Syntax Tree generator source files for extracting RESTful API url resource list. Requires you to have your nodejs environment set up. Details on how to set it up and get running can be accessed from this project repository: https://github.com/raml-org/raml-java-parser

## case_study_sources
Not required for this journal paper therefore can be safely ignored. The scope of the journal paper is limited to SOFL specification generation. However, it contains a minimal Django implementation of some of the API end points.

## DDD-and-Ecore
Contains case study source materials for our proposed approach, case study online salon booking system domain model and metamodel. We use Drawio tool to generate the PDF files for the domain model and metamodel.

## RAML
Contains a complete listing of our online salon booking system in RAML 1.0 specification.

## SOFL
Contains the targetted output of our proposed approach which are implicit SOFL specifications of the case study online salon booking system RESTful API. In addition, it contains an excel sheet with test cases of our API specifications and a representation each API SOFL process in _Process Functional Scenario_ forms for specification animation and testing.

## Threat-Modelling
Contains ADTree files generated for the case study threat modeling activities that is step 3 of our proposed approach
