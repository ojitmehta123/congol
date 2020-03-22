import congol.cogol as cgol
import json
import numpy as np
from nose.tools import *


with open("config/config.json") as c:
    config = json.load(c)
        
rows = config ["rows"]
cols = config ["cols"]
hold_time = config ["timeHold"]
stills = config ["stills"]
max_iter = config ["maxIter"]
display_char = config["displayChar"]

def testBlockPeriod():
    o = cgol.Gol()
    o.game = np.array(stills["Block"])
    o.setBoard()
    t1 = o.board
    o.playOneMove()
    assert (t1 == o.board).all
    assert rows == o.rows
    assert cols == o.cols

def testTubPeriod():
    o = cgol.Gol()
    o.game = np.array(stills["Tub"])
    o.setBoard()
    t1 = o.board
    o.playOneMove()
    assert (t1 == o.board).all
    assert rows == o.rows
    assert cols == o.cols

def testToadPeriod():
    o = cgol.Gol()
    o.game = np.array(stills["Toad"])
    o.setBoard()
    t1 = o.board
    o.playOneMove()

    assert (t1 != o.board).any
    assert rows == o.rows
    assert cols == o.cols

    o.playOneMove()
    assert (t1 == o.board).all

def testBlinkerPeriod():
    o = cgol.Gol()
    o.game = np.array(stills["Blinker"])
    o.setBoard()
    t1 = o.board
    o.playOneMove()

    assert (t1 != o.board).any
    assert rows == o.rows
    assert cols == o.cols

    o.playOneMove()
    assert (t1 == o.board).all

def testPulsarPeriod():
    o = cgol.Gol()
    o.game = np.array(stills["Pulsar"])
    o.setBoard()

    t1 = o.board
    o.playOneMove()

    assert (t1 != o.board).any
    assert rows == o.rows
    assert cols == o.cols

    o.playOneMove()
    assert (t1 != o.board).any
    assert rows == o.rows
    assert cols == o.cols

    o.playOneMove()
    assert (t1 == o.board).all
    assert rows == o.rows
    assert cols == o.cols
    
    