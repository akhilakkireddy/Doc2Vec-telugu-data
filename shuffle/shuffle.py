import random
import itertools
fo1= open("trainedVectors.txt","r")
fo2= open("tags.txt","r")
vectors,tags = [],[]
for line in fo1:
	vectors.append(line.strip())
for line in fo2:
	tags.append(line.strip())
combined = zip(vectors,tags)
random.shuffle(combined)
random.shuffle(combined)
vectors[:],tags[:] = zip(*combined)
fo1.close()
fo2.close()
count = 0
with open("trainData.txt","a") as f1, open("trainTags.txt","a") as f2, open("testData.txt","a") as f3,open("testTags.txt","a") as f4:
	for v,t in itertools.izip(vectors,tags):
		count += 1
		if count<=25:
			f1.write(v+"\n")
			f2.write(t+"\n")
		else:
			f3.write(v+"\n")
			f4.write(t+"\n")

f1.close()
f2.close()
f3.close()
f4.close()
