# Secret Message
**Purpose**   - A technical ability exercise.

## Overview
This is my first Python project which was the technical test in a Job Application.  It demonstrates my flexability in applying skills to new languages and technologies.

### Specification
Task - To write a short routine to accept the URL of a Google Document website, the site will contain a table with the following columns :-
1. **X-Coordinate** - This is the characters X-Coordinate final position.
2. **Character** - This is the character to be printed.
3. **Y-Coordinate** - This is the characters Y-Coordinate final position.

When the characters are printed at the correct coordinates a secret Message will be displayed in Uppercase letters, and should be completed in either Javascript or Python.

### Solution
1. **showMessage(URL)** - The Entry Method Accepts the URL parameter & calls the appropriate methods in turn.
2. **getData(URL)** - Gets the Data from the response of the URL request and returns the string docData.
3. **parseGoogleDocData(docData)** - Creates & populates a dictionary using the coordinates as the indexes and Character as the value stored. returns message dictionary object.
4. **printSecretMessage(message)** - Prints the Characters at the coordinates revealing the message in the console.

## License
See the [MIT](LICENSE) license for rights and limitations under the conditions of the license.
