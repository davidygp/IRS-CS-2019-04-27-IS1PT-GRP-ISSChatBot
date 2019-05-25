from flask import Flask, request, make_response, jsonify
import os
import pandas as pd
import util

# Add comment
app = Flask(__name__)

# *****************************
# Intent Handlers funcs : START
# *****************************

filepath = "./data/simple_text_response.csv"
database_fp = "./data/database.xlsx"

simple_text_response_df = pd.read_csv(filepath, header=0)
program_df = pd.read_excel(database_fp, "program")
gradProg_df = pd.read_excel(database_fp, "gradProg")
stackableProg_df = pd.read_excel(database_fp, "stackableProg")
executiveProg_df = pd.read_excel(database_fp, "executiveProg")
module_df = pd.read_excel(database_fp, "module")
lecturer_df = pd.read_excel(database_fp, "lecturer")

def extract_from_df(intent_name, df):
    for i in range(len(df)):
        if df["intent_name"][i] == intent_name:
            return df.at[i, "text_response"]


def getLocationIntentHandler():
    return extract_from_df("GetLocationIntent", simple_text_response_df)
    #"The Heng Mui Keng Campus can be found at: 29 Heng Mui Keng Terrace, Singapore 119620. Please visit https://www.iss.nus.edu.sg/about-us/getting-to-nus-iss for more info"
    
    
def getContactIntentHandler():
    return extract_from_df("GetContactIntent", simple_text_response_df)
    #"For General Enquiries, please email isstraining@nus.edu.sg, For Graduate Programme Enquiries, please email isspostgrad@nus.edu.sg or call 66013161"


def getProgramsatISS(UserType): 
    names_list = []
    for name in program_df["Name_Cleaned"]:
        names_list.append(name)
    text = "hi %s. ISS offers a range of programs suited to different professional needs. Details are %s. Any program you want to know about?" %(UserType, ", ".join(names_list))
    return text


def getMastersProgramsListing():
    count = len(gradProg_df["Name_Cleaned"])
    names_list = []
    for name in gradProg_df["Name_Cleaned"]:
        names_list.append(name)
    text = "ISS offers %s. The name of the Masters Programs are %s. Which Masters Programs would you want to know about?" %(count, ", ".join(names_list))
    return text


def getExecProgramlisting():
    count = len(executiveProg_df["Name"])
    names_list = []
    for name in executiveProg_df["Name"]:
        names_list.append(name)
    text = "ISS offers %s. The name of the Executive Programs are %s. Which Executive Programs would you want to know about?" %(count, ", ".join(names_list))
    return text


def getSkillbasedCourseListing(UserType, SkillCourselisting):
    names_list = []
    for i in range(module_df.shape[0]):
        if SkillCourselisting.lower().replace(" ","") in module_df.iloc[i]["Discipline"].lower().replace(" ",""):
            names_list.append(module_df.iloc[i]["Name_Cleaned"])
    text = "%s the related courses for %s are the following: %s" %(UserType, SkillCourselisting, ", ".join(names_list))
    return text


def getStackablePgm():
    count = len(stackableProg_df["Name"])
    names_list = []
    for name in stackableProg_df["Name"]:
        names_list.append(name)
    text = "ISS offers %s. The name of the Stackable Programs are %s. Which Stackable Programs would you want to know about?" %(count, ", ".join(names_list))
    return text


def getMastersProgramModuleListing(UserType, MastersProgramModulelisting):
    for i in range(gradProg_df.shape[0]):
        if MastersProgramModulelisting in gradProg_df.iloc[i]["Name"]:
            Name_Clean = gradProg_df.iloc[i]["Name_Cleaned"]
            Module = gradProg_df.iloc[i]["Module"]
            text = "%s the related courses for %s are the following: %s" %(UserType, Name_Clean, Module)
            return text
    return "Apologies, we do not have that data in our database as of now."


def getexecprogmodulelisting(UserType, ExecProgramModulelisting):
    for i in range(executiveProg_df.shape[0]):
        if ExecProgramModulelisting in executiveProg_df.iloc[i]["Name"]:
            Name = executiveProg_df.iloc[i]["Name"]
            Module = executiveProg_df.iloc[i]["Module"]
            text = "%s the related courses for %s are the following: %s" %(UserType, Name, Module)
            return text
    return "Apologies, we do not have that data in our database as of now."


def getStackableProgramModuleListing(UserType, stackableprogrammodulelisting):
    for i in range(stackableProg_df.shape[0]):
        if stackableprogrammodulelisting in stackableProg_df.iloc[i]["Name"]:
            Name = stackableProg_df.iloc[i]["Name"]
            Module = stackableProg_df.iloc[i]["Module"]
            text = "%s the related courses for %s are the following: %s" %(UserType, Name, Module)
            return text
    return "Apologies, we do not have that data in our database as of now."


def getfeesgrantsfinancingappenrollprogrammoduledegree(Module, progtype, search_item):
    if progtype == "":
        search_df = gradProg_df
    elif progtype == "MastersPgm":
        search_df = gradProg_df
    elif progtype == "StackablePgm":
        search_df = stackableProg_df
    elif progtype == "ExecPgm":
        search_df = executiveProg_df
    else:
        search_df = gradProg_df
    
    for i in range(search_df.shape[0]):
        if Module in search_df.iloc[i]["Name"]:
            search_text = search_df.iloc[i][search_item]
            if search_text is None or pd.isnull(search_text):
                return "Apologies, we do not have that data in our database as of now."
            elif len(search_text) >= 1:
                return search_text
            else:
                return "Apologies, we do not have that data in our database as of now."


def getStaffListingbyCategory(StaffCategory):
    names_list = []
    for i in range(lecturer_df.shape[0]):
        if StaffCategory in lecturer_df.iloc[i]["Category_Cleaned"]:
            names_list.append(lecturer_df.iloc[i]["Name"])
    if len(names_list) == 0:
        return "Apologies, we do not have that data in our database as of now."
    else:
        text = "For %s. The staff names are %s. Which staff would you want to know about?" %(StaffCategory, ", ".join(names_list))
        return text
    

def getlecturerinfo(StaffCategory, givenname, lastname):
    first_last_lower = givenname.lower().replace(" ","")+lastname.lower().replace(" ","")
    last_first_lower = lastname.lower().replace(" ","")+givenname.lower().replace(" ","")
    for i in range(lecturer_df.shape[0]):
        Name_lower = lecturer_df.iloc[i]["Name"].lower().replace(" ","")
        if StaffCategory == "":
            if first_last_lower in Name_lower or last_first_lower in Name_lower:
                Name = lecturer_df.iloc[i]["Name"]
                Profile = lecturer_df.iloc[i]["Profile"]
                text = "%s %s's profile is this: %s" %(StaffCategory, Name, Profile)
                return text
        else:
            if StaffCategory in lecturer_df.iloc[i]["Category"] and (first_last_lower in Name_lower or last_first_lower in Name_lower):
                Name = lecturer_df.iloc[i]["Name"]
                Profile = lecturer_df.iloc[i]["Profile"]
                text = "%s %s's profile is this: %s" %(StaffCategory, Name, Profile)
                return text
    return "Apologies, we do not have that data in our database as of now."

# ***************************
# Intent Handlers funcs : END
# ***************************

# *****************************
# WEBHOOK MAIN ENDPOINT : START
# *****************************
@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req["queryResult"]["intent"]["displayName"]
    print(req)
 
    ## Mapping of intent names from front-end (Dialogflow) to back-end (Python)
    """
    Answers the following intents:
    5.  ProgramsatISS                           (Done)
    6.  MastersProgramsListing                  (Done)
    7   ExecProgramlisting                      (Not invoked from front end.)
    8   SkillbasedCourseListing                 (Done)
    9   StackablePgm                            (Not invoked from front end.)
    10. MastersProgramModuleListing             (Done)
    11. execprogmodulelisting                   (Done)
    12. StackableProgramModuleListing           (Done)
    13. feesprogrammoduledegree                 (Done)
    14. grants-financing-programmoduledegree    (Partial, grants vs financing?)
    15. app-enroll-programmoduledegree          (Partial, apply vs enroll?)
    16. StaffListingbyCategory                  (Done)
    17. lecturerinfo                            (Done, the selection of names is iffy)
    """

    # Maps the naming from Dialogflow into the backend
    MastersProgramModulelisting_dict = {
        "SE":"master-of-technology-in-software-engineering",
        "EBA":"master-of-technology-in-enterprise-business-analytics",
        "KE":"master-of-technology-in-knowledge-engineering",
        "IS":"master-of-technology-in-intelligent-systems",
        "DL":"master-of-technology-in-digital-leadership",
        "SA":"graduate-diploma-in-systems-analysis"
    }

    if intent_name == "GetLocationIntent" :
        response_text = getLocationIntentHandler()
    elif intent_name == "GetContactIntent" :
        response_text = getContactIntentHandler()
    elif intent_name == "ProgramsatISS":
        UserType = req["queryResult"]["outputContexts"][0]["parameters"]["UserType"]
        response_text = getProgramsatISS(UserType)
    elif intent_name == "MastersProgramsListing":
        response_text = getMastersProgramsListing()
    elif intent_name == "ExecProgramlisting":
        response_text = "Sorry, data is not present in the database yet."
    elif intent_name == "SkillbasedCourseListing":
        UserType = req["queryResult"]["outputContexts"][0]["parameters"]["UserType"]
        SkillCourselisting = req["queryResult"]["parameters"]["SkillCourselisting"]
        print("Input parameters are UserType: %s and SkillCourselisting: %s" %(UserType, SkillCourselisting))
        response_text = getSkillbasedCourseListing(UserType, SkillCourselisting)
    elif intent_name == "StackablePgm":
        response_text = getStackablePgm()
    elif intent_name == "MastersProgramModuleListing":
        UserType = req["queryResult"]["outputContexts"][0]["parameters"]["UserType"]
        MastersProgramModulelisting = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
        print("Input parameters are UserType: %s and MastersProgramModulelisting: %s" %(UserType, MastersProgramModulelisting))
        response_text = getMastersProgramModuleListing(UserType, MastersProgramModulelisting)
    elif intent_name == "execprogmodulelisting":
        UserType = req["queryResult"]["outputContexts"][0]["parameters"]["UserType"]
        ExecProgramModulelisting = req["queryResult"]["parameters"]["ExecProgramModulelisting"]
        print("Input parameters are UserType: %s and ExecProgramModulelisting: %s" %(UserType, ExecProgramModulelisting))
        response_text = getexecprogmodulelisting(UserType, ExecProgramModulelisting)
    elif intent_name == "StackableProgramModuleListing":
        UserType = req["queryResult"]["outputContexts"][0]["parameters"]["UserType"]
        stackableprogrammodulelisting = req["queryResult"]["parameters"]["stackableprogrammodulelisting"]
        print("Input parameters are UserType: %s and stackableprogrammodulelisting: %s" %(UserType, stackableprogrammodulelisting))
        response_text = getStackableProgramModuleListing(UserType, stackableprogrammodulelisting)
    elif intent_name == "feesprogrammoduledegree":
        try:
            progtype = req["queryResult"]["parameters"]["progtype"]
            if progtype == "":
                Module = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
            elif progtype == "MastersPgm":
                Module = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
            elif progtype == "StackablePgm":
                Module = req["queryResult"]["parameters"]["stackableprogrammodulelisting"]
            elif progtype == "ExecPgm":
                Module = req["queryResult"]["parameters"]["ExecProgramModulelisting"]
            else:
                Module = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
            print("Input parameters are Module: %s and progtype: %s and search_item: %s" %(Module, progtype,"Cost"))
            response_text = getfeesgrantsfinancingappenrollprogrammoduledegree(Module, progtype, "Cost")
        except:
            response_text = "Sorry, unable to find such a program, please try saying it in a different way."
    elif intent_name == "grants-financing-programmoduledegree":
        try:
            progtype = req["queryResult"]["parameters"]["progtype"]
            if progtype == "":
                Module = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
            elif progtype == "MastersPgm":
                Module = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
            elif progtype == "StackablePgm":
                Module = req["queryResult"]["parameters"]["stackableprogrammodulelisting"]
            elif progtype == "ExecPgm":
                Module = req["queryResult"]["parameters"]["ExecProgramModulelisting"]
            else:
                Module = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
            print("Input parameters are Module: %s and progtype: %s and search_item: %s" %(Module, progtype,"Financing"))
            response_text = getfeesgrantsfinancingappenrollprogrammoduledegree(Module, progtype, "Financing")
        except:
            response_text = "Sorry, unable to find such a program, please try saying it in a different way."
    elif intent_name == "app-enroll-programmoduledegree":
        try:
            progtype = req["queryResult"]["parameters"]["progtype"]
            if progtype == "":
                Module = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
            elif progtype == "MastersPgm":
                Module = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
            elif progtype == "StackablePgm":
                Module = req["queryResult"]["parameters"]["stackableprogrammodulelisting"]
            elif progtype == "ExecPgm":
                Module = req["queryResult"]["parameters"]["ExecProgramModulelisting"]
            else:
                Module = MastersProgramModulelisting_dict[req["queryResult"]["parameters"]["MastersProgramModulelisting"]]
            print("Input parameters are Module: %s and progtype: %s and search_item: %s" %(Module, progtype,"Apply"))
            response_text = getfeesgrantsfinancingappenrollprogrammoduledegree(Module, progtype, "Apply")
        except:
            response_text = "Sorry, unable to find such a program, please try saying it in a different way."
    elif intent_name == "StaffListingbyCategory":
        try:
            StaffCategory = req["queryResult"]["parameters"]["StaffCategory"]
            print("Input parameters are StaffCategory: %s" %(StaffCategory))
            response_text = getStaffListingbyCategory(StaffCategory)
        except:
            response_text = "Sorry, unable to find such a program, please try saying it in a different way."
    elif intent_name == "lecturerinfo":
        try:
            StaffCategory = req["queryResult"]["parameters"]["StaffCategory"]
        except:
            StaffCategory = ""
        try:
            givenname = req["queryResult"]["parameters"]["given-name"]
        except:
            givenname = ""
        try:
            lastname = req["queryResult"]["parameters"]["last-name"]
        except:
            lastname = ""
        response_text = getlecturerinfo(StaffCategory, givenname, lastname)
    else:
        response_text = "No intent matched"

    # Send this response to Dialogflow.
    return make_response(jsonify({'fulfillmentText': response_text}))

# ***************************
# WEBHOOK MAIN ENDPOINT : END
# ***************************

if __name__ == '__main__':

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)