from pymongo import MongoClient

# Replace with your full connection URI
url = "mongodb+srv://gautampm2006:%23ILOVEMYCOUNTRY@cluster0.lwlizjm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(url)
    client.admin.command('ping')  # Ping the server
    print("✅ Connected to MongoDB Atlas!")
except Exception as e:
    print("❌ Connection failed:", e)
