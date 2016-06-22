# Person

## Description
This class represents people at Codecool, containing mentors and students and candidates.

## Parent class
None

## Attributes

* ```first_name```
  * data type: string
  * description: stores people's first names
* ```last_name```
  * data type: string
  * description: stores people's last names
* ```year_of_birth```
   * data type: integer
   * description: stores the year when they born
* ```gender```
  * data type: string
  * description: stores people's gender
* ```motivation_level```
    * data type: string
    * description: stores people's motivation levels
* ```in_school```
    * data type: boolean
    * description: shows that they are in the class or not
* ```happy```
    * data type: boolean
    * description: stores people's happiness levels

## Class methods

None

## Static methods

### ```come_to_school```

Modify the boolean in_school, happy, motivation_level, studied attributes for students and mentors as well.

#### Arguments

* ```mentors```
   * data type: list (containing Mentor objects)
   * description: stores the mentors of the class
* ```students```
  * data type: list (containing Student objects)
  * description: stores the students of the class

#### Return value

* ```mentors```
   * data type: list (containing Mentor objects)
   * description: stores the mentors of the class
* ```students```
  * data type: list (containing Student objects)
  * description: stores the students of the class

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None
