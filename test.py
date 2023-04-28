print("Hello World!")
# name = input("enter your name?")
# print(f"hello {name}")

name = "hello"

print(name[0])

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(f"set before remove{s}")
print(f"s length is {len(s)}")

s.remove(4)
print(f" set after remove {s}")
print(f"s length is {len(s)}")

# for
friends = ["tom", "jack", "harry"]
test = len(friends)
for i in range(test):
    print(friends[i])

# for
for i in range(6):
    print(i)

# for
for i in range(1, 10):
    print(i)

number = int(input("number?"))

if number > 0:
    print(f"{number} is greater than zero")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero ")
