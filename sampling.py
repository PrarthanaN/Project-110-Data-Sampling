import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

df = pd.read_csv("med_data.csv")
data = df["reading_time"].tolist()

def r_set_o_mean(counter):
    d_set = []
    for i in range(0,counter):
        r_index = random.randint(0,len(data)-1)
        val = data[r_index]
        d_set.append(val)
    mean = statistics.mean(d_set)
    return mean

def show_fig(m_list):
    df = m_list
    mean  = statistics.mean(df)
    fig = ff.create_distplot([df],["reading_time"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    m_list = []
    for i in range(0,1000):
        s_o_mean = r_set_o_mean(100)
        m_list.append(s_o_mean)
    show_fig(m_list)
    mean = statistics.mean(m_list)
    print("Mean of Sapling Distribution",mean)

setup()
population_mean = statistics.mean(data) 
print("population mean:- ", population_mean)
population_stdev = statistics.stdev(data)
print("Population Stdev:- ", population_stdev)

def standard_deviation(): 
    mean_list = [] 
    for i in range(0,1000): 
        set_of_means= r_set_o_mean(100) 
        mean_list.append(set_of_means) 
    std_deviation = statistics.stdev(mean_list) 
    print("Standard deviation of sampling distribution:- ", std_deviation) 
standard_deviation()