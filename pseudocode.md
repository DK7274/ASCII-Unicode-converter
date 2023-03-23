FUNCTION ASCIIUnicodeConvert():  
 * INPUT from user
 * IF input is not ASCII char:
   * PRINT that the input is invalid
   * RETURN to start of function
 * IF input is less than 0:
   * PRINT that the input is invalid
   * RETURN to start of function
 * PRINT the converted characters as unicode
 * RETURN to start of program

FUNCTION UnicodeASCIIConvert():  
* INPUT from user 
  * IF length of char is greater than 1:
    * CREATE array to store ASCII values
    * FOR each char:
      * CONVERT char to ASCII value using ord() function
      * ADD the ASCII value to created array
    * JOIN the array together and PRINT to user
    * CALL the start() function
  * ELSE IF length of char is 0:
    * PRINT that the input is invalid and to try again
    * RETURN to start of function
  * PRINT the converted characters ASCII
  * RETURN to the start of the program

FUNCTION start():
 * PRINT Title (ASCII-Unicode converter)
 * ASK user to enter either ASCII or UNICODE
 * IF user input is 'unicode':
   * CALL ASCIIUnicodeConvert()
 * ELIF user input is ASCII:
    * CALL UnicodeASCIIConvert()
 * ELSE:
   * PRINT input is invalid and to try again
   * RETURN to start of function

CALL start():
  