"""
Script untuk test generate project dari generate_gui.py
Test langsung generate_summary() dari AIWorker class
"""
import sys
from pathlib import Path

# Add ai_worker to path
sys.path.insert(0, str(Path(__file__).parent))

from ai_worker.generate_gui import AIWorker

def test_generate():
    """Test generate project"""
    print("="*60)
    print("Test Generate Project (GUI Version)")
    print("="*60)
    print()
    
    # Setup worker dengan showcase enabled
    worker = AIWorker(
        auto_push=False,  # Disable auto push untuk test
        push_to_showcase=True,  # Enable showcase
        showcase_repo_path="../Project-Showcase"
    )
    
    # Setup status callback untuk melihat progress
    def status_callback(msg):
        # Handle emoji untuk Windows console
        try:
            print(f"[STATUS] {msg}")
        except UnicodeEncodeError:
            # Remove emoji jika tidak bisa di-print
            safe_msg = msg.encode('ascii', 'ignore').decode('ascii')
            print(f"[STATUS] {safe_msg}")
    
    worker.status_callback = status_callback
    
    print("Starting generation...")
    print("-" * 60)
    
    try:
        # Generate project
        result = worker.generate_summary()
        print()
        print("-" * 60)
        print("="*60)
        print("Test complete!")
        print("="*60)
        print()
        print(f"Result: {result}")
        print()
        print("Check the following locations:")
        print("1. Project-Showcase/projects/")
        print("2. Project-Showcase/public/projects/")
        print()
        print("If push_to_showcase is enabled, check GitHub:")
        print("https://github.com/MarioSitepu/Jack-s-Cards")
        
    except Exception as e:
        print()
        print("="*60)
        print("ERROR occurred!")
        print("="*60)
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_generate()

