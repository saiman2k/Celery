#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: sainadh

Source:
    
'''

# Import necessary modules
 
from celery import Celery
from time import sleep
from fpdf import FPDF 
import pymongo


app = Celery('tasks', broker='amqp://localhost',backend='mongodb+srv://saiman2k:pswd1234@cluster0.fpqun.mongodb.net/test')

@app.task
def pdf():
    sleep(2)
    pdf = FPDF()    
   
    pdf.add_page() 

    pdf.set_font("Arial", size = 15) 
  
    f = open("/home/saiman2k/tact/dataset/my-text.txt", "r") 
  
    for x in f: 
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
   
    pdf.output("/home/saiman2k/tact/dataset/cel-pdf.pdf")   


def startpy():
    #pdf.delay()
    pass

if __name__ == '__main__':
    startpy()