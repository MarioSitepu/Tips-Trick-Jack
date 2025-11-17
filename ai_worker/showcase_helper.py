"""
Showcase Helper untuk Push ke Repo Showcase Terpisah
"""
import subprocess
import os
import shutil
from pathlib import Path
from datetime import datetime


def push_to_showcase_repo(
    source_project_dir,
    showcase_repo_path,
    github_token=None,
    branch="main",
    repo_url=None
):
    """
    Copy project ke repo showcase dan push ke GitHub
    
    Args:
        source_project_dir: Path ke folder project yang baru di-generate
        showcase_repo_path: Path ke repo showcase lokal (atau akan di-clone jika tidak ada)
        github_token: GitHub token untuk push
        branch: Branch untuk push (default: main)
        repo_url: URL repo showcase (untuk clone jika belum ada)
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        source_path = Path(source_project_dir)
        if not source_path.exists():
            return False, f"Source project not found: {source_project_dir}"
        
        showcase_path = Path(showcase_repo_path)
        
        # Clone repo jika belum ada
        if not showcase_path.exists() or not (showcase_path / ".git").exists():
            if not repo_url:
                return False, "Showcase repo not found and no repo_url provided"
            
            print(f"📦 Cloning showcase repo from {repo_url}...")
            try:
                # Clone repo
                if github_token and "github.com" in repo_url:
                    # Format URL dengan token
                    if repo_url.startswith("https://"):
                        if "@" not in repo_url:
                            repo_part = repo_url.replace("https://github.com/", "").replace(".git", "")
                            repo_url = f"https://x-access-token:{github_token}@github.com/{repo_part}.git"
                    elif repo_url.startswith("git@"):
                        repo_part = repo_url.replace("git@github.com:", "").replace(".git", "")
                        repo_url = f"https://x-access-token:{github_token}@github.com/{repo_part}.git"
                
                subprocess.run(
                    ["git", "clone", repo_url, str(showcase_path)],
                    check=True,
                    capture_output=True,
                    timeout=60
                )
                print(f"✅ Cloned showcase repo to {showcase_path}")
            except Exception as e:
                return False, f"Failed to clone showcase repo: {str(e)}"
        
        # Pastikan di git repo
        if not (showcase_path / ".git").exists():
            return False, f"Not a git repository: {showcase_path}"
        
        # Copy project folder ke showcase repo
        project_name = source_path.name
        dest_project_dir = showcase_path / "projects" / project_name
        
        # Buat folder projects jika belum ada
        (showcase_path / "projects").mkdir(exist_ok=True)
        
        # Copy folder project
        if dest_project_dir.exists():
            shutil.rmtree(dest_project_dir)
        shutil.copytree(source_path, dest_project_dir)
        
        print(f"📋 Copied project {project_name} to showcase repo")
        
        # Update gallery index (akan dibuat oleh generate_gallery_index)
        generate_gallery_index(showcase_path)
        
        # Git add, commit, push
        try:
            # Configure git user
            subprocess.run(
                ["git", "config", "user.name", "AI-Bot"],
                cwd=showcase_path,
                capture_output=True,
                timeout=5
            )
            subprocess.run(
                ["git", "config", "user.email", "ai-bot@example.com"],
                cwd=showcase_path,
                capture_output=True,
                timeout=5
            )
            
            # Add files
            subprocess.run(
                ["git", "add", "projects/", "index.html"],
                cwd=showcase_path,
                capture_output=True,
                timeout=10
            )
            
            # Check if there are changes
            result = subprocess.run(
                ["git", "diff", "--cached", "--quiet"],
                cwd=showcase_path,
                capture_output=True,
                timeout=5
            )
            
            if result.returncode == 0:
                # Check untracked files
                result2 = subprocess.run(
                    ["git", "ls-files", "--others", "--exclude-standard", "projects/", "index.html"],
                    cwd=showcase_path,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if not result2.stdout.strip():
                    return True, "No changes to commit"
            
            # Commit
            commit_msg = f"🎨 Add project: {project_name}"
            result = subprocess.run(
                ["git", "commit", "-m", commit_msg],
                cwd=showcase_path,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                if "nothing to commit" in result.stdout.lower() or "nothing to commit" in result.stderr.lower():
                    return True, "No changes to commit"
                return False, f"Commit failed: {result.stderr}"
            
            # Update remote URL dengan token jika perlu
            if github_token:
                result = subprocess.run(
                    ["git", "remote", "get-url", "origin"],
                    cwd=showcase_path,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                if result.returncode == 0:
                    remote_url = result.stdout.strip()
                    if "github.com" in remote_url and "x-access-token" not in remote_url:
                        if remote_url.startswith("https://"):
                            if "@" not in remote_url:
                                repo_part = remote_url.replace("https://github.com/", "").replace(".git", "")
                                new_url = f"https://x-access-token:{github_token}@github.com/{repo_part}.git"
                                subprocess.run(
                                    ["git", "remote", "set-url", "origin", new_url],
                                    cwd=showcase_path,
                                    capture_output=True,
                                    timeout=5
                                )
            
            # Push
            result = subprocess.run(
                ["git", "push", "origin", branch],
                cwd=showcase_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                return True, f"Successfully pushed {project_name} to showcase repo"
            else:
                error_msg = result.stderr or result.stdout
                if "already up to date" in error_msg.lower():
                    return True, "Already up to date"
                return False, f"Push failed: {error_msg}"
                
        except Exception as e:
            return False, f"Git operation failed: {str(e)}"
            
    except Exception as e:
        return False, f"Error: {str(e)}"


def generate_gallery_index(showcase_repo_path):
    """
    Generate index.html gallery untuk menampilkan semua project
    
    Args:
        showcase_repo_path: Path ke repo showcase
    """
    showcase_path = Path(showcase_repo_path)
    projects_dir = showcase_path / "projects"
    
    if not projects_dir.exists():
        projects_dir.mkdir(parents=True, exist_ok=True)
    
    # Scan semua project folders
    projects = []
    for project_folder in sorted(projects_dir.iterdir(), reverse=True):
        if project_folder.is_dir():
            html_file = project_folder / "index.html"
            if html_file.exists():
                # Parse tanggal dari nama folder (format: YYYY-MM-DD-HH-MM)
                folder_name = project_folder.name
                try:
                    date_part = folder_name.split("-")[:3]  # YYYY-MM-DD
                    time_part = folder_name.split("-")[3:5] if len(folder_name.split("-")) >= 5 else ["00", "00"]
                    date_str = "-".join(date_part)
                    time_str = ":".join(time_part)
                    display_date = f"{date_str} {time_str}"
                except:
                    display_date = folder_name
                
                projects.append({
                    "name": folder_name,
                    "date": display_date,
                    "path": f"projects/{folder_name}/index.html"
                })
    
    # Generate HTML gallery
    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎨 AI Generated Projects Gallery</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        header {{
            text-align: center;
            color: white;
            padding: 40px 20px;
            margin-bottom: 40px;
        }}
        
        header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }}
        
        header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .stats {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 30px;
            color: white;
            text-align: center;
        }}
        
        .stats span {{
            font-size: 1.5em;
            font-weight: bold;
        }}
        
        .projects-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }}
        
        .project-card {{
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
            text-decoration: none;
            color: inherit;
            display: block;
        }}
        
        .project-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        }}
        
        .project-preview {{
            width: 100%;
            height: 200px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3em;
            color: white;
        }}
        
        .project-info {{
            padding: 20px;
        }}
        
        .project-info h3 {{
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1.3em;
        }}
        
        .project-info p {{
            color: #666;
            font-size: 0.9em;
        }}
        
        .project-date {{
            color: #999;
            font-size: 0.85em;
            margin-top: 10px;
        }}
        
        footer {{
            text-align: center;
            color: white;
            padding: 30px;
            margin-top: 40px;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2em;
            }}
            
            .projects-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎨 AI Generated Projects Gallery</h1>
            <p>Koleksi proyek HTML/CSS yang di-generate secara otomatis oleh AI</p>
        </header>
        
        <div class="stats">
            <p>Total Projects: <span>{len(projects)}</span></p>
        </div>
        
        <div class="projects-grid">
"""
    
    # Add project cards
    for project in projects:
        html_content += f"""            <a href="{project['path']}" target="_blank" class="project-card">
                <div class="project-preview">🎨</div>
                <div class="project-info">
                    <h3>{project['name']}</h3>
                    <p>AI Generated Project</p>
                    <div class="project-date">📅 {project['date']}</div>
                </div>
            </a>
"""
    
    html_content += """        </div>
        
        <footer>
            <p>Generated automatically by AI Daily Summary Generator</p>
            <p>Last updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
        </footer>
    </div>
</body>
</html>
"""
    
    # Write index.html
    index_path = showcase_path / "index.html"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Generated gallery index with {len(projects)} projects")

