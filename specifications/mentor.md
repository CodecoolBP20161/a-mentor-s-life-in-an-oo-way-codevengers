# Mentor

## Description
This class represents the awesome mentors of Codecool and their attributes

## Parent class
Mentor class inherits from Person class

## Attributes
* ```nickname```
    * data type: string
    * description: stores the nickname of each mentor

## Class methods

### ```create_by_csv```

Reads Person attributes as a csv file

#### Arguments

* The csv file's name

#### Return value

A list of mentor


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```do_morning_gym```

Executes morning gym if ```energy_level``` is low for the instances of students and mentors

#### Arguments
* ```students```
    * data type: list
    * description: contains the instances of every student


* ```mentors```
    * data type: list
    * description: contains the instances of every mentor

#### Return value
None

### ```daily_agenda```

Tells the daily agenda and increases the ```motivation_level```

#### Arguments
* ```students```
    * data type: list
    * description: contains the instances of every student

#### Return value
None

### ```mentoring```

Helps a student to understand the know-how of the magic called programming and this makes the student ```Happy```, increases ```knowledge_level``` and ```motivation_level``` while decreasing ```energy_level```

#### Arguments
* ```student```
    * data type: object
    * description: holds the object of a student

#### Return value
None

### ```interview```
Performs a quick and decisive talk with an instance of the ```Candidate```.
Sets the value of ```candidate_in_school``` to True.
If the mentors accept the candidate, (they all roll one) the candidates ```self.motivation_level``` increases, otherwise decreases.

#### Arguments
* ```candidate```
    * data type: object
    * description: holds the object of a candidate
* ```mentors```
    * data type: list
    * description: holds the objects of mentors

#### Return value
None
