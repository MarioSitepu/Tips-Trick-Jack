"""
Script untuk menambahkan AI-Daily-Summary.exe ke Windows Startup
"""
import os
import sys
import shutil
from pathlib import Path
import winreg


def get_startup_folder():
    """Get Windows Startup folder path"""
    startup = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
    return startup


def add_to_startup_folder(exe_path):
    """Add EXE to Windows Startup folder via shortcut"""
    try:
        import win32com.client
        
        startup_folder = get_startup_folder()
        startup_folder.mkdir(parents=True, exist_ok=True)
        
        # Create shortcut
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut_path = startup_folder / "AI-Daily-Summary.lnk"
        shortcut = shell.CreateShortCut(str(shortcut_path))
        shortcut.Targetpath = str(exe_path)
        shortcut.WorkingDirectory = str(exe_path.parent)
        shortcut.IconLocation = str(exe_path)
        shortcut.save()
        
        return True, f"Shortcut created: {shortcut_path}"
    except ImportError:
        # Fallback: Copy EXE to startup folder (less ideal but works)
        startup_folder = get_startup_folder()
        startup_folder.mkdir(parents=True, exist_ok=True)
        
        startup_exe = startup_folder / exe_path.name
        if startup_exe.exists():
            return False, f"Already exists: {startup_exe}"
        
        shutil.copy2(exe_path, startup_exe)
        return True, f"Copied to: {startup_exe}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def add_to_registry(exe_path):
    """Add EXE to Windows Registry (Run key)"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        
        winreg.SetValueEx(
            key,
            "AI-Daily-Summary",
            0,
            winreg.REG_SZ,
            str(exe_path)
        )
        
        winreg.CloseKey(key)
        return True, "Added to Windows Registry"
    except Exception as e:
        return False, f"Registry error: {str(e)}"


def remove_from_startup_folder():
    """Remove from Startup folder"""
    try:
        startup_folder = get_startup_folder()
        shortcut_path = startup_folder / "AI-Daily-Summary.lnk"
        exe_path = startup_folder / "AI-Daily-Summary.exe"
        
        removed = False
        if shortcut_path.exists():
            shortcut_path.unlink()
            removed = True
        
        if exe_path.exists():
            exe_path.unlink()
            removed = True
        
        if removed:
            return True, "Removed from Startup folder"
        else:
            return False, "Not found in Startup folder"
    except Exception as e:
        return False, f"Error: {str(e)}"


def remove_from_registry():
    """Remove from Windows Registry"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        
        try:
            winreg.DeleteValue(key, "AI-Daily-Summary")
            winreg.CloseKey(key)
            return True, "Removed from Windows Registry"
        except FileNotFoundError:
            winreg.CloseKey(key)
            return False, "Not found in Registry"
    except Exception as e:
        return False, f"Registry error: {str(e)}"


def is_in_startup():
    """Check if already in startup"""
    startup_folder = get_startup_folder()
    shortcut_path = startup_folder / "AI-Daily-Summary.lnk"
    exe_path = startup_folder / "AI-Daily-Summary.exe"
    
    in_folder = shortcut_path.exists() or exe_path.exists()
    
    in_registry = False
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_READ
        )
        try:
            winreg.QueryValueEx(key, "AI-Daily-Summary")
            in_registry = True
        except FileNotFoundError:
            pass
        winreg.CloseKey(key)
    except:
        pass
    
    return in_folder or in_registry


def main():
    """Main function"""
    print("=" * 60)
    print("AI-Daily-Summary - Startup Setup")
    print("=" * 60)
    print()
    
    # Find EXE
    script_dir = Path(__file__).parent
    exe_path = script_dir / "dist" / "AI-Daily-Summary.exe"
    
    if not exe_path.exists():
        # Try current directory
        exe_path = script_dir / "AI-Daily-Summary.exe"
        if not exe_path.exists():
            print("❌ Error: AI-Daily-Summary.exe not found!")
            print(f"   Searched in: {script_dir / 'dist'}")
            print(f"   Searched in: {script_dir}")
            print()
            print("Please run this script from the project root directory,")
            print("or specify the EXE path manually.")
            return
    
    exe_path = exe_path.resolve()
    print(f"✅ Found EXE: {exe_path}")
    print()
    
    # Check current status
    if is_in_startup():
        print("⚠️  Already in startup!")
        print()
        choice = input("Remove from startup? (y/n): ").lower()
        if choice == 'y':
            success1, msg1 = remove_from_startup_folder()
            success2, msg2 = remove_from_registry()
            if success1 or success2:
                print(f"✅ {msg1}")
                print(f"✅ {msg2}")
                print()
                print("Removed from startup successfully!")
            else:
                print(f"❌ {msg1}")
                print(f"❌ {msg2}")
        return
    
    # Ask user which method
    print("Choose method to add to startup:")
    print("1. Startup Folder (Recommended)")
    print("2. Windows Registry")
    print("3. Both")
    print()
    choice = input("Choice (1/2/3): ").strip()
    
    success = False
    messages = []
    
    if choice == "1" or choice == "3":
        success1, msg1 = add_to_startup_folder(exe_path)
        messages.append(msg1)
        if success1:
            success = True
    
    if choice == "2" or choice == "3":
        success2, msg2 = add_to_registry(exe_path)
        messages.append(msg2)
        if success2:
            success = True
    
    print()
    if success:
        print("✅ Successfully added to startup!")
        for msg in messages:
            print(f"   - {msg}")
        print()
        print("The application will start automatically when Windows boots.")
    else:
        print("❌ Failed to add to startup:")
        for msg in messages:
            print(f"   - {msg}")
        print()
        print("You may need to run as Administrator.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

