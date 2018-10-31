import gspread
from oauth2client.service_account import ServiceAccountCredentials
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import time

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Survey for AP Gov (Responses)").sheet1

Q1Results = sheet.col_values(2)
Q2Results = sheet.col_values(3)
Q3Results = sheet.col_values(4)
Q4Results = sheet.col_values(5)
Q5Results = sheet.col_values(6)
Q6Results = sheet.col_values(7)
Q7Results = sheet.col_values(8)
Q8Results = sheet.col_values(9)
Q9Results = sheet.col_values(10)
Q10Results = sheet.col_values(11)

#One graph per question, subsections for each demographic
#Title is the question

#results is a 2D array, don't forget
results = [Q1Results, Q2Results, Q3Results, Q4Results, Q5Results, Q6Results, Q7Results, Q8Results, Q9Results, Q10Results]
AgeGroup = results[0][1:]
Gender = results[1][1:]
Race = results[2][1:]

def getDemo(index):
	return [AgeGroup[index], Gender[index], Race[index]]

def addAge(demo, response):
	if response == "Yes" or response == "I support it":
		if demo == "10-19":
			AgeResults[0][0] = AgeResults[0][0] + 1
		elif demo == "20-29":
			AgeResults[1][0] = AgeResults[1][0] + 1
		elif demo == "30-39":
			AgeResults[2][0] = AgeResults[2][0] + 1
		elif demo == "40-49":
			AgeResults[3][0] = AgeResults[3][0] + 1
		elif demo == "50+":
			AgeResults[4][0] = AgeResults[4][0] + 1
	elif response == "No" or response == "I don't support it":
		if demo == "10-19":
			AgeResults[0][1] = AgeResults[0][1] + 1
		elif demo == "20-29":
			AgeResults[1][1] = AgeResults[1][1] + 1
		elif demo == "30-39":
			AgeResults[2][1] = AgeResults[2][1] + 1
		elif demo == "40-49":
			AgeResults[3][1] = AgeResults[3][1] + 1
		elif demo == "50+":
			AgeResults[4][1] = AgeResults[4][1] + 1
	elif "Yes, but" in response or "I support it, but" in response:
		if demo == "10-19":
			AgeResults[0][2] = AgeResults[0][2] + 1
		elif demo == "20-29":
			AgeResults[1][2] = AgeResults[1][2] + 1
		elif demo == "30-39":
			AgeResults[2][2] = AgeResults[2][2] + 1
		elif demo == "40-49":
			AgeResults[3][2] = AgeResults[3][2] + 1
		elif demo == "50+":
			AgeResults[4][2] = AgeResults[4][2] + 1
	elif "No, but" in response or "I don't support it, but" in response:
		if demo == "10-19":
			AgeResults[0][3] = AgeResults[0][3] + 1
		elif demo == "20-29":
			AgeResults[1][3] = AgeResults[1][3] + 1
		elif demo == "30-39":
			AgeResults[2][3] = AgeResults[2][3] + 1
		elif demo == "40-49":
			AgeResults[3][3] = AgeResults[3][3] + 1
		elif demo == "50+":
			AgeResults[4][3] = AgeResults[4][3] + 1

def addGen(demo, response):
	if response == "Yes" or response == "I support it":
		if demo == "Male":
			GenderResults[0][0] = GenderResults[0][0] + 1
		elif demo == "Female":
			GenderResults[1][0] = GenderResults[1][0] + 1
		elif demo == "Prefer not to say":
			GenderResults[2][0] = GenderResults[2][0] + 1
	elif response == "No" or response == "I don't support it":
		if demo == "Male":
			GenderResults[0][1] = GenderResults[0][1] + 1
		elif demo == "Female":
			GenderResults[1][1] = GenderResults[1][1] + 1
		elif demo == "Prefer not to say":
			GenderResults[2][1] = GenderResults[2][1] + 1
	elif "Yes, but" in response or "I support it, but":
		if demo == "Male":
			GenderResults[0][2] = GenderResults[0][2] + 1
		elif demo == "Female":
			GenderResults[1][2] = GenderResults[1][2] + 1
		elif demo == "Prefer not to say":
			GenderResults[2][2] = GenderResults[2][2] + 1
	elif "No, but" in response or "I don't support it, but" in response:
		if demo == "Male":
			GenderResults[0][3] = GenderResults[0][3] + 1
		elif demo == "Female":
			GenderResults[1][3] = GenderResults[1][3] + 1
		elif demo == "Prefer not to say":
			GenderResults[2][3] = GenderResults[2][3] + 1

def addRac(demo, response):
	if demo == "Native American":
		if response == "Yes" or response == "I support it":
			RaceResults[0][0] = RaceResults[0][0] + 1
		elif response == "No" or response == "I don't support it":
			RaceResults[0][1] = RaceResults[0][1] + 1
		elif "Yes, but" in response or "I support it, but" in response:
			RaceResults[0][2] = RaceResults[0][2] + 1
		elif "No, but" in response or "I don't support it, but" in response:
			RaceResults[0][3] = RaceResults[0][3] + 1
	elif demo == "Asian":
		if response == "Yes" or response == "I support it":
			RaceResults[1][0] = RaceResults[1][0] + 1
		elif response == "No" or response == "I don't support it":
			RaceResults[1][1] = RaceResults[1][1] + 1
		elif "Yes, but" in response or "I support it, but" in response:
			RaceResults[1][2] = RaceResults[1][2] + 1
		elif "No, but" in response or "I don't support it, but" in response:
			RaceResults[1][3] = RaceResults[1][3] + 1
	elif demo == "African American":
		if response == "Yes" or response == "I support it":
			RaceResults[2][0] = RaceResults[2][0] + 1
		elif response == "No" or response == "I don't support it":
			RaceResults[2][1] = RaceResults[2][1] + 1
		elif "Yes, but" in response or "I support it, but" in response:
			RaceResults[2][2] = RaceResults[2][2] + 1
		elif "No, but" in response or "I don't support it, but" in response:
			RaceResults[2][3] = RaceResults[2][3] + 1
	elif demo == "Hispanic":
		if response == "Yes" or response == "I support it":
			RaceResults[3][0] = RaceResults[3][0] + 1
		elif response == "No" or response == "I don't support it":
			RaceResults[3][1] = RaceResults[3][1] + 1
		elif "Yes, but" in response or "I support it, but" in response:
			RaceResults[3][2] = RaceResults[3][2] + 1
		elif "No, but" in response or "I don't support it, but" in response:
			RaceResults[3][3] = RaceResults[3][3] + 1
	elif demo == "White":
		if response == "Yes" or response == "I support it":
			RaceResults[4][0] = RaceResults[4][0] + 1
		elif response == "No" or response == "I don't support it":
			RaceResults[4][1] = RaceResults[4][1] + 1
		elif "Yes, but" in response or "I support it, but" in response:
			RaceResults[4][2] = RaceResults[4][2] + 1
		elif "No, but" in response or "I don't support it, but" in response:
			RaceResults[4][3] = RaceResults[4][3] + 1
	elif demo == "White":
		if response == "Yes" or response == "I support it":
			RaceResults[5][0] = RaceResults[5][0] + 1
		elif response == "No" or response == "I don't support it":
			RaceResults[5][1] = RaceResults[5][1] + 1
		elif "Yes, but" in response or "I support it, but" in response:
			RaceResults[5][2] = RaceResults[5][2] + 1
		elif "No, but" in response or "I don't support it, but" in response:
			RaceResults[5][3] = RaceResults[5][3] + 1
	elif demo == "Prefer not to answer":
		if response == "Yes" or response == "I support it":
			RaceResults[6][0] = RaceResults[6][0] + 1
		elif response == "No" or response == "I don't support it":
			RaceResults[6][1] = RaceResults[6][1] + 1
		elif "Yes, but" in response or "I support it, but" in response:
			RaceResults[6][2] = RaceResults[6][2] + 1
		elif "No, but" in response or "I don't support it, but" in response:
			RaceResults[6][3] = RaceResults[6][3] + 1

for answers in range(3, len(results)):
	question = results[answers][0]
	responses = results[answers][1:]
	AgeResults = [[0 for i in range(4)]for i in range(5)]
	GenderResults = [[0 for i in range(4)]for i in range(3)]
	RaceResults = [[0 for i in range(4)]for i in range(7)]
	for i in range(len(responses)):
		current = responses[i]
		demos = getDemo(i)
		for demo in demos:
			if demo == "Male" or demo == "Female" or demo == "Prefer not to say":
				addGen(demo, current)
			elif demo == "10-19" or demo == "20-29" or demo == "30-39" or demo == "40-49" or demo == "50+":
				addAge(demo, current)
			elif demo == "Native American" or demo == "Asian" or demo == "African American" or demo == "Hispanic" or demo == "White" or demo == "Prefer not to answer":
				addRac(demo, current)
	print(GenderResults)
	GenResp = [0 for i in range(4)]
	AgeResp = [0 for i in range(4)]
	RaceResp = [0 for i in range(4)]
	choices = ['Agree', 'Disagree', 'Agree with conditions', 'Disagree with conditions']
	for i in range(4):
		temp1 = [GenderResults[0][i], GenderResults[1][i], GenderResults[2][i]]
		temp2 = [AgeResults[0][i], AgeResults[1][i], AgeResults[2][i], AgeResults[3][i], AgeResults[4][i]]
		temp3 = [RaceResults[0][i], RaceResults[1][i], RaceResults[2][i], RaceResults[3][i], RaceResults[4][i], RaceResults[5][i], RaceResults[6][i]]
		GenResp[i] = go.Bar(x = ['Male', 'Female', 'Prefer not to say'],y = temp1, text = temp1, textposition = 'auto', name = choices[i])
		AgeResp[i] = go.Bar(x = ['10-19', '20-29', '30-39', '40-49', '50+'],y = temp2, text = temp2, textposition = 'auto', name = choices[i])
		RaceResp[i] = go.Bar(x = ['Native American', 'Asian', 'African American', 'Hispanic', 'White', 'Prefer not to answer'],y = temp3, text = temp3, textposition = 'auto',name = choices[i])
	plotly.offline.plot({"data": GenResp,"layout": go.Layout(title=question)}, auto_open=True)
	time.sleep(1)
	plotly.offline.plot({"data": AgeResp,"layout": go.Layout(title=question)}, auto_open=True)
	time.sleep(1)
	plotly.offline.plot({"data": RaceResp,"layout": go.Layout(title=question)}, auto_open=True)
	time.sleep(1)