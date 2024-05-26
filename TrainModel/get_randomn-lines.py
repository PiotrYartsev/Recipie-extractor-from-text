#for each txt file, open it up and choose 20 random non empty lines longer than 5 characters
#write all of these lines to a single cvs file, with the line as one column and leave the other column blank
#this will be used to train the model
import os
import random


txt_files = [f for f in os.listdir("extractedtotext") if f.endswith('.txt')]

for txt_file in txt_files:
    with open(os.path.join("extractedtotext", txt_file), 'r') as file:
        lines = file.readlines()
        random_lines = random.sample(lines, 20)
        with open("random_lines.csv", 'a') as csv_file:
            for line in random_lines:
                if len(line) > 5:
                    csv_file.write("'{}'".format(line.strip()) + ",\n")
