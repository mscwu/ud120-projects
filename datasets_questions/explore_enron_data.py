#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# print number of features for each person
print "number of features: ", len(enron_data["SKILLING JEFFREY K"])
# print number of person of interest
print "number of pois: ",len([people for people in enron_data if enron_data[people]["poi"]])

# print stock belongs to James Prentice

for keys in enron_data["PRENTICE JAMES"].keys():
    print keys
print enron_data["PRENTICE JAMES"]["total_stock_value"]

# print email messages from Wesley Colwell to poi

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# print stock options exercised by Jeffery Skilling
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# find number of people with quantified salary and known email address
n_salary = 0
n_email = 0
for person in enron_data.keys():
    if enron_data[person]["salary"] != "NaN":
        n_salary += 1
    if enron_data[person]["email_address"] != "NaN":
        n_email += 1

print "number of quantified salary", n_salary
print "number of know email address", n_email

# number of people with NAN for their total payments and percentage
nan_total_payments = 0
for person in enron_data.keys():
    if enron_data[person]["total_payments"] == "NaN":
        nan_total_payments += 1
print "number of people with NaN for their total payments: ", nan_total_payments
print "and the percentage is: ", float(nan_total_payments)/len(enron_data.keys())

# number of pois in the dataset having NaN for their total payments and the percentage
nan_poi_total_payments = 0
for person in enron_data.keys():
    if enron_data[person]["total_payments"] == "NaN" and enron_data[person]["poi"]:
        nan_poi_total_payments += 1
print "number of poi with NaN for their total payments: ", nan_poi_total_payments
print "and the percentage is: ", float(nan_poi_total_payments)/len(enron_data.keys())

