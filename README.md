# LITAF
Compiler and programming language "litaf"
Last compiled date: May 08, 2019
# The language
## Structure
Litad follows a minimum structure, so be sure to follow it before compiling it!
```
litaf start:
  main is int
  
  end
end
```
This is the minimum structure, anything you want to run with ths structure can be placed inside `main`
## Variable Declaration
Litaf nahdles 5 types for data types: `int`, `flo`, `cha`, `str`, and `boo`. For declaring a variable you just simply type the type you want your variable to be and then a name for the variable. Multiple variable declarations is supported.
```
int varInt
str stringOne, stringTwo, stringThree
```
Variables use camelCase, with optinal numbers at the end, so any time you want to declare a variable remember to follow the format!
```
flo taxDiscount35
boo pass
cha bloodType
```
## Global Variables
Litaf supports global variables, for using them you just need to declare them outside of `main` and all global variables must be declared before any function.
```
litaf start:
  int globalVar1, globalVar2
  fun FOO() is void
    out(globalVar2)
  end
  main is int
    int x
    globalVar1 = 100
    globalVar2 = 250
    x = globalVar1 - globalVar2
    FOO()
  end
end
```
## Main Function
Litaf uses a main function called `main`. From `main` you can call other functions or classes, or execute many statements.
```
litaf start:
  main is int
    str helloWorld
    helloWorld = "Hello World!"
    out(helloWorld)
  end
end
```
## Custom Functions
Eventhough you have `main` you can create other functions. The structure for creating a function is the following:
```
litaf start:
  fun FOO() is void
  end
  fun BAR(int y) is int
    int result
    result = y + 10
  with result end
  main is int
    int x
    FOO()
    x = BAR(5)
  end
end
```
Functions can be from any of the types already listed or can be `void`. All functions should be placed before `main` and a function can only call a function that was previously defined.
Note that function names are in UPPERCASE and can implement `_`, like `FOO_BAR()`
## Inputs and Outputs
For input you can use the `in()` and for output `out()`
```
int payment
in(payment)
out(payment * 0.5, " ", payment, "n/")
```
Remember that for inputs, the variables passed as parameters must exist and for outputs, the printed data comes together, if you want to separate them you can use `" "` as parameters. For printing a newline, you must pass as parameter the string `"n/"`
## Cycles
Cycles are implemented using Loop cycle. Loop cycles works as a traditional While, but its structure implies a control variable just like a For Loop.
```
int low
low = 0
loop from low upto 10
  out(low)
by +2 end
```
Loop cycle is inclusive, meaning you can go from `x` either `upto` (<=) or `downto` (>=) `y`.
## Decisions
Litaf uses IF-ELSIF-ELSE structure, where ELSIF and ELSE are optional when using IF, but `end` must be present to indicate the end of the conditional
```
if (globalLow == 8)
  out(8)
end
if (globalHigh != 7)
  out("Not 7")
else
  out("Seven")
end
if(globalLow < globalHigh)
  out("No")
elsif(globalLow == globalHigh)
  out("Yes")
else
  out("Nah")
end
```
## Classes
Litaf is working on implementing classes. They should be placed before global variables and follow this structure```
```
litaf start: 
  class Person is
    attributes:
      public str name
      private cha bloodType
    end
    methods:
      public Person() is Person
      end
    end
  end
  class Doctor from Person is
    attributes:
      public str title
      private int id
    end
    methods:
      public Doctor() is Doctor
      end
    end
  end
  main is int
    Person per
    Doctor doc
  end
end
```
In this example, Person and Doctor are classes. Doctor inherits all Person attributes.
# The Compiler
For compiling litaf you just need pipenv installed. Then after cloning the repo and having that directory open in terminal, you can:
```
python litaf.py file.lit
```
Litaf only accepys `.lit` extensions
