"""
Git Helper untuk Auto Commit & Push
"""
import subprocess
import os
from pathlib import Path


def is_git_repo(path):
    """Check if path is a git repository"""
    git_dir = Path(path) / ".git"
    return git_dir.exists() or git_dir.is_dir()


def get_git_root(path):
    """Get git root directory"""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=path,
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return Path(result.stdout.strip())
    except:
        pass
    return None


def git_commit_and_push(repo_path, files_to_add=None, commit_message=None, token=None, branch=None):
    """
    Commit dan push ke GitHub
    
    Args:
        repo_path: Path ke repository
        files_to_add: List file/folder untuk di-add (default: ["data/", "projects/"])
        commit_message: Commit message (default: auto-generated)
        token: GitHub token untuk push (opsional, bisa pakai credential helper)
        branch: Branch untuk push (default: current branch)
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        from datetime import datetime
        
        # Default values
        if files_to_add is None:
            files_to_add = ["data/", "projects/"]
        
        if commit_message is None:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_message = f"🤖 AI update: New project created at {now}"
        
        # Check if git is available
        try:
            subprocess.run(["git", "--version"], capture_output=True, check=True, timeout=5)
        except:
            return False, "Git not found. Please install Git."
        
        # Check if in git repo
        git_root = get_git_root(repo_path)
        if not git_root:
            return False, "Not a git repository. Please run in a git repository."
        
        # Configure git user (if not set)
        try:
            subprocess.run(
                ["git", "config", "user.name", "AI-Bot"],
                cwd=git_root,
                capture_output=True,
                timeout=5
            )
            subprocess.run(
                ["git", "config", "user.email", "ai-bot@example.com"],
                cwd=git_root,
                capture_output=True,
                timeout=5
            )
        except:
            pass
        
        # Get current branch if not specified
        if branch is None:
            result = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                cwd=git_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                branch = result.stdout.strip()
            else:
                branch = "main"
        
        # Add files
        for file_path in files_to_add:
            full_path = git_root / file_path
            if full_path.exists():
                try:
                    subprocess.run(
                        ["git", "add", file_path],
                        cwd=git_root,
                        capture_output=True,
                        timeout=10
                    )
                except Exception as e:
                    return False, f"Failed to add {file_path}: {str(e)}"
        
        # Check if there are changes
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=git_root,
            capture_output=True,
            timeout=5
        )
        
        # Check untracked files
        result2 = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"] + files_to_add,
            cwd=git_root,
            capture_output=True,
            text=True,
            timeout=5
        )
        
        has_changes = result.returncode != 0 or (result2.returncode == 0 and result2.stdout.strip())
        
        if not has_changes:
            return True, "No changes to commit"
        
        # Commit
        try:
            result = subprocess.run(
                ["git", "commit", "-m", commit_message],
                cwd=git_root,
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode != 0:
                # Check if commit failed because no changes
                if "nothing to commit" in result.stdout.lower() or "nothing to commit" in result.stderr.lower():
                    return True, "No changes to commit"
                return False, f"Commit failed: {result.stderr}"
        except Exception as e:
            return False, f"Commit error: {str(e)}"
        
        # Push
        try:
            # Get remote URL
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                cwd=git_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                return False, "No remote 'origin' found"
            
            remote_url = result.stdout.strip()
            
            # If token provided, update remote URL
            if token:
                # Extract repo from remote URL
                if "github.com" in remote_url:
                    # Format: https://github.com/user/repo.git
                    # Or: git@github.com:user/repo.git
                    if remote_url.startswith("https://"):
                        # Replace with token
                        if "@" in remote_url:
                            # Already has credentials
                            repo_part = remote_url.split("@")[1]
                        else:
                            repo_part = remote_url.replace("https://", "").replace("github.com/", "")
                        
                        remote_url = f"https://x-access-token:{token}@github.com/{repo_part}"
                    elif remote_url.startswith("git@"):
                        # SSH format, convert to HTTPS
                        repo_part = remote_url.replace("git@github.com:", "").replace(".git", "")
                        remote_url = f"https://x-access-token:{token}@github.com/{repo_part}.git"
                    
                    # Update remote URL
                    subprocess.run(
                        ["git", "remote", "set-url", "origin", remote_url],
                        cwd=git_root,
                        capture_output=True,
                        timeout=5
                    )
            
            # Push
            result = subprocess.run(
                ["git", "push", "origin", branch],
                cwd=git_root,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                return True, f"Successfully pushed to {branch}"
            else:
                error_msg = result.stderr or result.stdout
                # Check if already up to date
                if "already up to date" in error_msg.lower():
                    return True, "Already up to date"
                return False, f"Push failed: {error_msg}"
                
        except Exception as e:
            return False, f"Push error: {str(e)}"
            
    except Exception as e:
        return False, f"Error: {str(e)}"

