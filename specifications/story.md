# Story

## Description
This is the story of our demo.

* In the morning every ```Mentor``` and a randomly selected number of ```Student```s arrive to the school.
They have their attributes set by code and/or by data from csv file.
* The ```Mentor```s detect the average ```energy_level``` of the ```Student```s and initiate ```do_morning_gym```
if neccessary, which raises the ```Student```s' ```energy_level```.
* Then the ```Mentor```s tell the ```daily_agenda```, which raises the ```motivation_level``` of the students.
* If a ```Student```'s ```studied_level``` value is ```False``` their ```motivation_level```
slightly decreases. The ```Mentor```s do ```mentoring``` to
set ```Student```s' ```studied_level``` ```True``` and increase the ```motivation_level```.
* The ```Student```s ```learn``` which increases their ```knowledge_level```
and slightly decrease their ```energy_level```.
* The ```lunch``` ```leisure_events``` refill the ```energy_level```.
* After ```lunch``` the ```student```s continue to ```learn``` with the ```mentoring``` help of one ```Mentor```.
* The second ```Mentor``` does ```private_mentoring_events``` which sets
the attending ```Student```s ```come_to_school``` value ```True``` and increases
their ```knowledge_level```.
* The third ```Mentor``` does ```interview``` which sets ```Candidate```s' ```come_to_school``` ```True```,
checks their ```application_code``` and decides whether they are ```accepted``` or not.
* When all these events finished, ```leisure_events``` are initiated, where ```Mentor```s
and ```Student```s attend randomly. This increases their ```motivation_level```.
* Then they all go home and set their ```come_to_school``` value to ```False``` and
refill their ```energy_level```.

The End.
