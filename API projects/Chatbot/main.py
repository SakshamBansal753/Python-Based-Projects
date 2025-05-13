from google import genai

client = genai.Client(api_key="AIzaSyCRoGg7peH1GInGwKSVbE4eD4P9898d_H8")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=input("Enter Your Question")
)
print(response.text)
