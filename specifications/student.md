# Student
# CodecoolClass

## Description
This class represents the students of Codecool, containing containing their knowledge, attributes and datas.

## Parent class
Person

## Attributes

* ```knowledge_level```
  * data type: integer
  * description : stores the student's level of knowledge

* ```energy_level```
  * data type: integer
  * description: stores the student's level of energy

* ```studied```
  * data type: boolean
  * description: stores the fact that the student did study or not


## Class methods

### ```create_by_csv```
Read persons attributes from the csv files.

### Arguments

The csv file's name.

### Return value

List of ```Student``` objects.

## Instance methods

### ```__init__```
The constructor of the object.

### Arguments

All of the arguments of parent class.

#### Return value
None

### ```learn```
Modify the level of the student's level of knowledge, energy and motivation.

#### Arguments

List of objects of the ```Student``` class.

#### Return value

List of objects of the ```Student``` class.
