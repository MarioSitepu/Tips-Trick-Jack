"""
Script untuk test generate project dan commit/push ke showcase repo
"""
import sys
from pathlib import Path

# Add ai_worker to path
sys.path.insert(0, str(Path(__file__).parent))

from ai_worker.generate import generate_summary

if __name__ == "__main__":
    print("="*60)
    print("Test Generate Project & Push to Showcase")
    print("="*60)
    print()
    
    print("Generating project...")
    try:
        generate_summary()
        print()
        print("="*60)
        print("Test complete! Check console output above for details.")
        print("="*60)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

