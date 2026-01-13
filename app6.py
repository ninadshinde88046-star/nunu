import google.generativeai as genai
genai.configure(api_key="AIzaSyAKY4w4CYmLlSxWFTUa4jEI4gh061fgyZY")
for m in genai.list_models():
    print(m.name)