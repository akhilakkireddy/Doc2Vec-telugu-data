# Doc2Vec-telugu-data

data.txt:

Has input data for training. Has 50 songs. Each document/song is in a single line.

tags.txt :

This file contains tag of 0/1 ~ sad/happy for each song in data.txt

testdata.txt:

File contains a test data point which is actually from happy song.

Procedure:

-> Train the model:

	python make_doc2vec_model.py
	
	This generates model.tel file where the model is saved.
	
-> Write trained vectors to a file:

	python vector.py
	
	This generates onlyVectors.txt where vectors for each document 	are generated.

-> [optional]  Visualise song and it's vector:
	
	python vector+song.py
	
	This generates vector+song+visualise.txt where song and it's corresponding vector can be visualised.

-> convert to Format suitable to classifier in matlab:
	
	python vec2CF.py
	
	This generates the file trainInput.txt which is a input to the 	classifier for training.
