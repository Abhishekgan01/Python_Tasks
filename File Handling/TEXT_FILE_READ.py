f = open("demo.txt", "r")
for x in f:
  print(x)

print(f.readline())
print(f.tell())

for _ in range(5):
    print("Hello, World!")
