"""
Build script untuk convert Python script ke .exe
Menggunakan PyInstaller
"""
import os
import sys
import subprocess
from pathlib import Path

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        return True
    except ImportError:
        return False

def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    dependencies = [
        "pyinstaller",
        "pystray",
        "pillow"
    ]
    
    for dep in dependencies:
        print(f"Installing {dep}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

def build_exe():
    """Build executable"""
    script_dir = Path(__file__).parent
    worker_dir = script_dir / "ai_worker"
    script_path = worker_dir / "generate_gui.py"
    
    if not script_path.exists():
        print(f"Error: Script not found at {script_path}")
        return False
    
    print(f"Building executable from {script_path}...")
    
    # PyInstaller command
    # Note: --add-data format is "source;destination" for Windows, "source:destination" for Linux/Mac
    import platform
    separator = ";" if platform.system() == "Windows" else ":"
    
    # Check if icon exists
    icon_path = script_dir / "icon.ico"
    icon_arg = f"--icon={icon_path}" if icon_path.exists() else "--icon=NONE"
    
    cmd = [
        "pyinstaller",
        "--name=Gemini-Project-Generator",
        "--onefile",  # Single executable file
        "--windowed",  # No console window (GUI only)
        icon_arg,  # Use icon.ico if available
        f"--add-data=data{separator}data",  # Include data folder
        "--hidden-import=pystray",
        "--hidden-import=PIL",
        "--hidden-import=PIL._tkinter_finder",
        "--hidden-import=tkinter",
        "--hidden-import=google.generativeai",  # Gemini API
        "--hidden-import=google.generativeai.types",  # Gemini types
        "--hidden-import=google.api_core",  # Google API core
        "--collect-all=pystray",  # Collect all pystray data
        "--collect-all=PIL",  # Collect all PIL data
        "--collect-all=google.generativeai",  # Collect all Gemini data
        str(script_path)
    ]
    
    try:
        subprocess.check_call(cmd, cwd=script_dir)
        print("\n" + "="*50)
        print("Build successful!")
        print("="*50)
        print(f"Executable location: {script_dir / 'dist' / 'Gemini-Project-Generator.exe'}")
        print("\nYou can now run Gemini-Project-Generator.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        return False

def main():
    """Main function"""
    print("="*50)
    print("Gemini Project Generator - EXE Builder")
    print("="*50)
    
    # Check PyInstaller
    if not check_pyinstaller():
        print("PyInstaller not found. Installing...")
        try:
            install_dependencies()
        except Exception as e:
            print(f"Failed to install dependencies: {e}")
            print("\nPlease install manually:")
            print("pip install pyinstaller pystray pillow")
            return
    
    # Build
    if build_exe():
        print("\n✅ Build completed successfully!")
        print("\nNext steps:")
        print("1. Find Gemini-Project-Generator.exe in the 'dist' folder")
        print("2. Copy it to your desired location")
        print("3. Make sure 'data' folder exists in the same directory")
        print("4. Set GEMINI_API_KEY environment variable (jika pakai AI)")
        print("5. Run the .exe file")
        print("\n📖 Untuk setup API key, lihat GEMINI_SETUP.md")
    else:
        print("\n❌ Build failed. Please check the errors above.")

if __name__ == "__main__":
    main()

