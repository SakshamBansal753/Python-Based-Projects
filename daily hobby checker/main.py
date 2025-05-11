import requests

from datetime import datetime
USERNAME="YOU CAN CREATE ANY NAME"
TOKEN_1="ANY RANDOM SET OF CHARACTERS"
ID="ANY NAME YOU WANT TO GIVE TO GRAPH"
PIXELA_ENDPOINT="https://pixe.la/v1/users"
param={
    "token":TOKEN_1,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#-------------------Step 1 create the user account remember after creation comment this two line------#
# response=requests.post(url=PIXELA_ENDPOINT,json=param)
# print(response.text)

graph_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
today=datetime.now()
graph_params={
    "id":ID,
    "name":"Cycling",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN_1
}
#-----------Step 2 do same thing as (1)--------------------#
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)\




pixel_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many km You cycle today")

}
#--------------------Step3----------------#
pixel_url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}"
responses=requests.post(url=pixel_url,json=pixel_params,headers=headers)
print(responses.text)




update_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"

new_data={
    "quantity":"8.9"
}
#------------------------Step 4------------------#



# responses=requests.put(url=update_endpoint,json=new_data,headers=headers)
# print(responses.text)