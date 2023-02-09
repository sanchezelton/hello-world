# Lesson 8:
# Loops (https://www.learnpython.org/en/Loops)
# based on lessons available at www.learnpython.org

# for loops can iterate over a given sequence, like lists
print("Primes from 2 thru 7")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
print()

# to specify a range to iterate over, use range:

# 0-4 (5 is non-inclusive)
print("Range up to 5 (non-inclusive)")
for x in range(5):
    print(x)
print()

# 3-5 (6 non-inclusive)
print("Range between 3 and 6 (non-inclusive)")
for x in range(3, 6):
    print(x)
print()

# 3-8 stepping by 2 (8 non-inclusive): e.g. 3, 5, 7
print("Range between 3 and 8 (non-inclusive), every other number")
for x in range(3, 8, 2):
    print(x)
print()

# range returns a list...while xrange returns an iterator (under python 2.x), which is more efficient.
# Note: xrange is DEPRECATED in favor of range. python3 no longer has xrange and range under py3 returns an iterator
# However, xrange should be known by py devs for py2.x purposes
# UNCOMMENT only for python 2.x for xrange
# print("xrange primes")
# for prime in xrange(5):
    # print(x)

# while loops repeat so long as the boolean condition is met
count = 0
print("While loop for 0 thru 4")
while (count < 5):
    print("Count is %d" % count)
    count += 1  # short hand for count = count + 1
print()


# break can exit a for loop or while loop. continue skips the currrent block and returns to the for or while statement:

count = 0
print("While loop for 0 thru 4 using break")
while True:
    print("Count is %d" % count)
    count += 1 # there is no "count++" incrementer in python
    if count >= 5:
        break
print()

# prints out odd numbers only
print("Odd numbers between 0 and 10 (non-inclusive)")
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
print()

# else CAN be used for loops

# prints out 0-4 then prints count value reached 5
count = 0
while (count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" % count)
print()

# prints out 1-4, but terminates thru break and does NOT invoke the else statement's print call.
for i in range(1, 10):
    if (i % 5 == 0):
        break
    print(i)
else:
    print("This is not printed because for loop is terminated because of the break but not due to fail in the condition")
print()

print("Exercise")

# Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any
# numbers that come after 237 in the sequence
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
# your code goes here
    if number == 237:
        break
    else:
        if number % 2 == 0:
            print(number)

