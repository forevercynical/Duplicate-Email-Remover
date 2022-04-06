import glob, json

# Reading all JSON Files From Input Folder
JSONFiles = glob.glob('Input/*.json')

FinalJSON = []
Total_Emails = 0

for file in JSONFiles:
    # Reading JSON File
    data = json.load(open(file))

    Total_Emails += len(data)

    for item in data:
        FinalJSON.append(item)

# Removing Duplicate Emails
FinalJSON = list({item['email']: item for item in FinalJSON}.values())


# Writing JSON Object to File in Output Folder
with open('Output/Final_JSON.json', 'w') as fp:
    json.dump(FinalJSON, fp, indent=4)

print('Total Emails in ' + str(len(JSONFiles)) + ' JSON Files: ' + str(Total_Emails))
print('Total Emails After Merging and Removing Duplicates: ' + str(len(FinalJSON)))
