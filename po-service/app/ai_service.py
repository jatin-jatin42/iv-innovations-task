from .database import mongo_collection
import datetime

async def generate_description(product_name: str, category: str):
    prompt = f"Write a professional 2-sentence marketing description for the following product: {product_name} in category {category}"
    # Simulated Gemini or OpenAI call implementation.
    # We will simulate successful completion.
    simulated_response = f"Introducing the {product_name}, a top-tier choice in {category}. Designed to elevate your experience, it combines innovation with unparalleled performance."

    # Log to MongoDB
    log_entry = {
        "product_name": product_name,
        "category": category,
        "prompt": prompt,
        "generated_description": simulated_response,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    
    await mongo_collection.insert_one(log_entry)

    return {"description": simulated_response}
