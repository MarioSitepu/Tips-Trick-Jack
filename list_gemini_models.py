"""
List available Gemini models
"""
import os
import sys
import google.generativeai as genai

# Fix encoding untuk Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ GEMINI_API_KEY not set!")
    exit(1)

genai.configure(api_key=api_key)

print("Available Gemini Models:")
print("=" * 50)

try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"✅ {model.name}")
            print(f"   Display Name: {model.display_name}")
            print(f"   Description: {model.description[:100] if model.description else 'N/A'}")
            print()
except Exception as e:
    print(f"❌ Error listing models: {e}")

