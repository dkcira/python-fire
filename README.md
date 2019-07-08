# python-fire
Python Fire: a library for automatically generating command line interfaces

pip install fire

# calling the method of a class
./example1.py  hello
./example1.py  hello David
./example1.py  hello David --interactive

# calling a function
./example2.py dorian

# multiple commands
./example3.py add 10 20
./example3.py multiply 10 20

# multiple commands with dict to map names
./example4.py add 10 20
./example4.py multiply 10 20

# with object of a class
./example5.py add 10 20
./example5.py multiply 10 20
./example5.py will print a help

# grouping commands
# the first one is not working for some reason
./example6.py run
./example6.py ingestion run
./example6.py digestion run
./example6.py digestion status

# airports module
https://github.com/trendct-data/airports.py
# accessing properties
./example7.py --code=JFK code
./example7.py --code=SJC name
./example7.py --code=ALB city
# upper works because 'city' is a string
./example7.py --code=ALB city upper

# Chaining function calls using class with methods that return self
./example8.py move 3 3 on __str__
./example8.py move 3 3 on move 3 6 on move 6 3 on move 6 6 on move 7 4 on move 7 5 on __str__
./example8.py move 3 3 on __str__ --size 20

# simpler hello world
./example9.py english
./example9.py spanish



Links
https://github.com/google/python-fire/blob/master/docs/guide.md
https://opensource.googleblog.com/2017/03/python-fire-command-line.html?utm_content=bufferf0f28&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer`
https://github.com/google/python-fire#python-fire

