#importing requires libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image #this is used to display image

# in this block of code we are essentially going to disp
# lay the image
image = Image.open("C:\\Users\\Dineshkumar\\OneDrive\\Desktop\\dna-nucleotide.jpg") #this is to open the image in our webapp in the variable image

st.image(image, use_column_width=True) #this is written so the image will be occupying the full space

st.write("""
# DNA NUCLEOTIDE  COUNT WEB APP

This app counts the nucleotide composition of query DNA!

***
""") # here header is written with # , *** is used to create a line

#in this block we are going to create text box to get the input
st.header('Enter the DNA sequence') #this will be displayed at the top
# we have to get the input
sequence_input = ">DNA Query \nGAACTACTAGGACTCAGGGTTACG\nGTACGCATTATAGCTAGCGCATGA\nACTACTACGAGTGTCGTCTACGTA" #sample input
sequence = st.text_area("Sequence input", sequence_input, height = 250) #this is useed to create textbox having header sequence input and it takes the values stored in variable sequence input 
sequence.splitlines() #this code splits the input according to the newline
#sequence # to print or display after splitting
sequence = sequence[1:] #this skips the first splitted line because index of that first line is 0
sequence = ''.join(sequence) #concatenates lists to string, this is  

st.write("""
***
"""
)

st.header('INPUT (DNA Query)') # the entered dna seq will be printed here
sequence

st.header('OUTPUT (DNA NUCLEOTIDE COUNT)') #it is the header to display the op

#print the dictionary
st.subheader('1. DICTIONARY') #subheader displays heading slightly less in size
def DNA_nucleotide_count(seq): #this is the custom func we create with name DNA_nucleotide_count and input argument is sequence
  d = dict([
            ('A',seq.count('A')),
            ('G',seq.count('G')),
            ('C',seq.count('C')),
            ('T',seq.count('T')),
  ]) #we are creating a dictionary containing the details of count which we calculate using .count function
  return d
X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

#lets now print the text , user readable form
st.subheader('2. TEXT')
st.write('There are '+ str(X['A']) + ' adenine (A)')
st.write('There are '+ str(X['G']) + ' guanine  (G)')
st.write('There are '+ str(X['C']) + ' cytosine (C)')
st.write('There are '+ str(X['T']) + ' thymine (T)')

#here we write code to display the dataframe for easily understanding by seeing it
st.subheader('3. DATA-FRAME') #sub heading for the df
df = pd.DataFrame.from_dict(X, orient = 'index') #in this we are gng to create a dataframe using the dictionary from the func which is oriented acc to its index
df = df.rename({0: 'count'}, axis= 'columns') #by default by running the above code the name of the column will be 0 so we have to rename it to count
df.reset_index(inplace=True) 
df = df.rename(columns = {'index': 'nucleotide'}) #similarly we write the heading for the nucleotide in column 
st.write(df)

# in this block we are going to display it in barchart
st.subheader('4. BAR CHART') #subheading for this
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
) #we r creating the bar chart using altair lib func and encoding the name for x axis as nucleotide and y axis as count 
p = p.properties(
    width=alt.Step(80) #this is width of the bar bcoz by default the bar will be thin
)
st.write(p)