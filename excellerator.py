import pandas
import json

excel_data_df = pandas.read_excel('example xlsx.xlsx', sheet_name='Sheet1')

thisisjson = excel_data_df.to_json(orient='records')

print('Excel Sheet to JSON:\n', thisisjson)

thisisjson_dict = json.loads(thisisjson)

with open('data.json', 'w') as json_file:
	json.dump(thisisjson_dict, json_file)
