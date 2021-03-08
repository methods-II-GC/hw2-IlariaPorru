#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 11:47:52 2021

@author: ilaria
"""

import argparse
import random
from typing import Iterator, List

#function
def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines
        
#function that makes it train, dev and test
def createTrainDevSplit(path, test, dev,train):
    print("+ Test : .", (test))
    print("+ Dev : .", (dev))
    print("+ Train : .", (train))

#create an empty list where test and validation data goes
    test = []
    dev = []
    train = []
    
    #how long the file is and reading file
def main(args: argparse.Namespace) -> None: 
    corpus = list(read_tags(args.input))
        
    pomodoro = int(len(corpus)*.8)
    guanciale = int(len(corpus)*.10)
#seeding
    random.seed(args.seed)
    #shuffles data so that it does not affect the result
    #slicing data according to the ratio 80/10/10
    random.shuffle(corpus)
    test1 = corpus[0:pomodoro]
    dev1 = corpus[pomodoro : (pomodoro + guanciale)]
    train1 = corpus[(pomodoro+ guanciale):]

#prints the lenght of each piece of data
    print("+ Training set size:", (len(train1)))
    print("+ Test set size:", (len(test1)))
    print("+ Development set size:", (len(dev1)))

#createTrainDevSplit(args.fileDir, args.testRatio, args.DevRatio)
    
    with open(args.train, "w") as spaghetti:
        spaghetti.write("train.")
        
    with open(args.dev, "w") as pizza:
        pizza.write("dev")
        
    with open(args.test, "w") as carbonara:
        carbonara.write("test")
        #can't figure out formatting
#this was given by Kyle
if __name__ == "__main__":
# declare arguments.
    parser = argparse.ArgumentParser()
#declare arguments & seeding
#optional argument
    parser.add_argument ("--seed", required = True)
    #rest of arguments - not optional
    parser.add_argument("input")
    parser.add_argument('--file', type=str, help="Directory of file to read the thing.")
    parser.add_argument('--testRatio', type=float, default=0.10,
                        help="Test to training ratio.")
    parser.add_argument('--devRatio', type=float, default=0.10,
                        help="Development to training ratio.")  
                      
# parse arguments and pass them to `main`.
    main(parser.parse_args())