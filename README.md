# code-kata-challenge

This repository contains all the code related to the Code Kata Challenge of AgileLab.


### 1 - Gilded Rose

The first challenge is called Gilded Rose, [here](gilded-rose/requirements.txt) are the requirements. \
The refactored version with the new features is present in [gilded_rose_refactored.py](gilded-rose/gilded_rose_refactored.py)

### 2 - Racing Car Katas

#### General Requirements

For this exercise, you should identify which SOLID principles are violated. For each exercise, you should identify which SOLID principles are not being followed by the code. There is only one class you are interested in writing tests for right now.

When you have some kind of test to lean on, refactor the code and make it testable. Take care when refactoring not to alter the functionality, or change interfaces which other client code may rely on. (Imagine there is client code in another repository that you can't see right now). Add more tests to cover the functionality of the particular class you've been asked to get under test.

#### [Tire Pressure Monitoring System](https://github.com/aleriboni/code-kata-challenge/blob/e826c8590b432c133ab27250c4ef25db85f42f1d/racing-car-katas/tire-pressure-monitoring)

##### Requirements

Write the unit tests for the Alarm class. The Alarm class is designed to monitor tire pressure and set an alarm if the pressure falls outside of the expected range. The Sensor class provided for the exercise fakes the behaviour of a real tire sensor, providing random but realistic values.

##### Solution

To define unit tests for Alarm class, it is necessary to go and test the following use cases:
* check that the alarm is turned off before checking on the sensor
* check that the alarm turns on when the maximum threshold is exceeded
* check that the alarm turns on when the minimum threshold is exceeded
* check that the alarm does not turn on when the pressure value is between the thresholds

By implementing the tests it is possible to notice the limitations of the legacy code: the sensor is instantiated within the Alarm class and from the outside there is no visibility of the pressure value.
To implement the tests it was necessary to patch the **psi_pressure_value** by simulating the cases presented earlier.

There are two SOLID principles violated:
* **Single Responsibility**: the check method of the Alarm class has both the task of retrieving the pressure value from the sensor and checking that it is between acceptable thresholds.
* **Dependency inversion**: the Alarm class (high level) depends on the Sensor class (low level). Dependency between classes must be replaced with abstractions.

In the general requirements it is specified not to change the interfaces. For this reason the signature of the **check** method was not changed: in the absence of this constraint the pressure value could have been passed as a parameter to the **check** method solving the problem related to the single responsibility principle.
To solve the problem related to dependency inversion, a **SensorInterface** interface was defined. Each class that implements such an interface must define the **get_psi_pressure** method.
A **PressureSensor** class implementing **SensorInterface** is instantiated within the Alarm class.

#### [Leaderboard](https://github.com/aleriboni/code-kata-challenge/blob/e826c8590b432c133ab27250c4ef25db85f42f1d/racing-car-katas/leaderboard)

##### Requirements

Write the unit tests for the Leaderboard class, including races with self-driving cars. The Leaderboard calculates driver points and rankings based on results from a number of races.

##### Solution

The following SOLID principles are violated in the legacy code:
* **Liskov substitution principle (LSP)**: the **SelfDrivingCar** subclass extends **Driver** by setting None as its name. Therefore, an abstract **AbstractDriver** class with an abstract **get_name** method was defined. The implementations of this abstract class have different fields that will be defined in the concrete subclasses.
* **Single responsibility principle (SRP)**: the **Race** class is responsible for assigning points and creating the name to **SelfDrivingCar**. This responsibility is moved to the **SelfDrivingCar** class.
* **Opening and closing principle (OCP)**: race **points** can be passed as a parameter so that the **Race** object can be extended to other types of races or rule changes. In order not to change the method signature, the current points are used as default values.
* **Dependency inversion**: the **LeaderBoard** class (high level) depends on the **Race** class (low level). Dependency between classes has been replaced with abstractions (**AbstractRace**).

To make the code more robust, we cover the case where a driver not present at the race is passed to the **points** method. It gets 0 points.
Also, if the _results_ list is greater than the _points_ list, extra drivers get 0 points.


#### [Text Converter](https://github.com/aleriboni/code-kata-challenge/blob/e826c8590b432c133ab27250c4ef25db85f42f1d/racing-car-katas/text-converter)

##### Requirements

Write the unit tests for the UnicodeFileToHtmlTextConverter class. The UnicodeFileToHtmlTextConverter class is designed to reformat a plain text file for display in a browser. There is an additional class "HtmlPagesConverter" which is slightly harder to get under test. It not only converts text in a file to html, it also supports pagination. It's meant as a follow up exercise.

##### Solution

The following SOLID principles are violated in the legacy code:
* Single responsibility principle (SRP): the **convert_to_html** method is responsible for reading the file and escaping each line (and string concatenation). The responsibility for reading the file has been delegated to an ad hoc **HtmlReader** class. In case of FileNotFoundError, for simplicity, the **read_file** methods returns an empty list. This approach makes the converter robust but is not suitable for a real use case because we lose error visibility
* **Opening and closing principle (OCP)**: the **Reader** should be passed as a parameter of **UnicodeFileToHtmlTextConverter**. In the general requirements it is specified not to change the interfaces. In the absence of this constraint the HtmlReader could have been passed as a field of **UnicodeFileToHtmlTextConverter** to be open for extension (and close for modification).

Other legacy code issues:
* File handling: opening the file is done via a context manager (**with open(...)**) so that it closes automatically in case of exceptions

