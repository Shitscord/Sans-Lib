import sanslib, os

if not os.path.exists("input"):
    os.makedirs("input")

if not os.path.exists("output"):
    os.makedirs("output")
    
for file in os.listdir("input"):
    print(file)
    print(sanslib.sans_eye("input/"+file,"output/"+file))