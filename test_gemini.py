"""
Test script untuk verifikasi Gemini API Key
Jalankan: python test_gemini.py
"""
import os
import sys

# Fix encoding untuk Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

def test_gemini():
    """Test koneksi ke Gemini API"""
    print("=" * 50)
    print("Testing Gemini API Connection")
    print("=" * 50)
    
    # Check API Key
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("\n❌ ERROR: API Key not found!")
        print("\nCara setup:")
        print("1. Dapatkan API key dari: https://aistudio.google.com/app/apikey")
        print("2. Set environment variable:")
        print("   Windows: set GEMINI_API_KEY=your-api-key")
        print("   Linux/Mac: export GEMINI_API_KEY=your-api-key")
        print("\n📖 Lihat GEMINI_SETUP.md untuk panduan lengkap")
        return False
    
    print(f"\n✅ API Key found: {api_key[:10]}...{api_key[-5:]}")
    
    # Check library
    try:
        import google.generativeai as genai
        print("✅ google-generativeai library installed")
    except ImportError:
        print("\n❌ ERROR: google-generativeai not installed!")
        print("Install dengan: pip install google-generativeai")
        return False
    
    # Configure
    try:
        genai.configure(api_key=api_key)
        print("✅ API configured")
    except Exception as e:
        print(f"\n❌ ERROR configuring API: {e}")
        return False
    
    # Test connection
    try:
        print("\n🔄 Testing connection to Gemini...")
        
        # Try different models (prioritize stable versions)
        models_to_try = [
            'gemini-2.5-flash',        # Stable Gemini 2.5 Flash
            'gemini-2.0-flash-001',    # Stable Gemini 2.0 Flash
            'gemini-2.0-flash',        # Gemini 2.0 Flash
            'gemini-2.0-flash-exp',    # Experimental (might have quota issues)
            'gemini-flash-latest',     # Latest Flash
        ]
        
        model_used = None
        last_error = None
        for model_name in models_to_try:
            try:
                print(f"   Trying {model_name}...")
                model = genai.GenerativeModel(model_name)
                response = model.generate_content("Say hello in one word!")
                model_used = model_name
                break
            except Exception as e:
                last_error = str(e)
                print(f"   ❌ {model_name} failed: {str(e)[:100]}")
                continue
        
        if not model_used:
            print("❌ ERROR: Could not connect to any Gemini model")
            if last_error:
                print(f"\nLast error: {last_error}")
            print("\nKemungkinan masalah:")
            print("1. API key tidak valid atau expired")
            print("2. Quota exceeded")
            print("3. Network connection issue")
            print("4. Model name tidak tersedia")
            return False
        
        print(f"✅ Connected to: {model_used}")
        print(f"✅ Response: {response.text}")
        
        print("\n" + "=" * 50)
        print("✅ SUCCESS! Gemini API is working!")
        print("=" * 50)
        print("\nAnda bisa menjalankan aplikasi sekarang:")
        print("  python ai_worker/generate.py")
        print("  atau")
        print("  python ai_worker/generate_gui.py")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nKemungkinan masalah:")
        print("1. API key tidak valid")
        print("2. Quota exceeded")
        print("3. Network connection issue")
        return False

if __name__ == "__main__":
    success = test_gemini()
    sys.exit(0 if success else 1)

