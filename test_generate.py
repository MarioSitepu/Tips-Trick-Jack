"""Test script untuk generate_summary"""
import sys
from pathlib import Path
from ai_worker.generate_gui import AIWorker

def test_generate():
    print("=" * 50)
    print("Testing Generate Summary")
    print("=" * 50)
    
    # Create worker dengan push_to_showcase enabled
    worker = AIWorker(push_to_showcase=True)
    
    print(f"\nConfiguration:")
    print(f"  - Push to showcase: {worker.push_to_showcase}")
    print(f"  - Showcase repo path: {worker.showcase_repo_path}")
    print(f"  - Data dir: {worker.data_dir}")
    
    # Resolve showcase path
    showcase_path = Path(worker.showcase_repo_path)
    if not showcase_path.is_absolute():
        base_dir = Path(__file__).parent
        showcase_path = base_dir.parent / showcase_path.replace("../", "")
    
    print(f"  - Showcase path resolved: {showcase_path}")
    print(f"  - Showcase path exists: {showcase_path.exists()}")
    
    # Test generate
    print(f"\n{'=' * 50}")
    print("Running generate_summary()...")
    print("=" * 50)
    
    try:
        result = worker.generate_summary()
        print(f"\n✅ Generate successful!")
        print(f"Result: {result}")
        
        # Check if files were created
        projects_dir = showcase_path / "projects"
        if projects_dir.exists():
            import os
            projects = [d for d in os.listdir(projects_dir) if os.path.isdir(projects_dir / d)]
            if projects:
                latest_project = sorted(projects)[-1]
                project_dir = projects_dir / latest_project
                print(f"\n📁 Latest project: {latest_project}")
                print(f"   Location: {project_dir}")
                
                html_file = project_dir / "index.html"
                css_file = project_dir / "style.css"
                print(f"   HTML exists: {html_file.exists()}")
                print(f"   CSS exists: {css_file.exists()}")
                
                # Check public/projects
                public_projects_dir = showcase_path / "public" / "projects" / latest_project
                if public_projects_dir.exists():
                    print(f"   Public/projects exists: {public_projects_dir.exists()}")
                    public_html = public_projects_dir / "index.html"
                    public_css = public_projects_dir / "style.css"
                    print(f"   Public HTML exists: {public_html.exists()}")
                    print(f"   Public CSS exists: {public_css.exists()}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"\n{'=' * 50}")
    print("Test completed!")
    print("=" * 50)

if __name__ == "__main__":
    test_generate()

