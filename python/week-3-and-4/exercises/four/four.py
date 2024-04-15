GA = float(input("Enter your GA grade: "))
GB = float(input("Enter your GB grade: "))

if GA < 0 or GB < 0:
  print("Error");
else:
  average = (GA * 0.30) + (GB * 0.70);
  if average >= 7.00:
    print("you don't need to do GC!!");
  else:
    print("you need to do GC!!");