"""
Script untuk membuat icon aplikasi Gemini Project Generator
Membuat icon ICO dari PIL Image dengan tema purple-pink gradient
"""
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

def create_app_icon():
    """Create application icon with Gemini/AI theme"""
    # Create base image (256x256 for high quality)
    size = 256
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Background gradient (purple to pink) - simplified
    # Draw solid background first
    draw.ellipse([0, 0, size, size], fill=(147, 51, 255, 255))
    
    # Draw main circle background
    margin = 20
    draw.ellipse([margin, margin, size-margin, size-margin], 
                 fill=(147, 51, 255, 255), outline=(255, 20, 147, 255), width=8)
    
    # Draw AI/Robot icon (simplified Gemini symbol)
    center_x, center_y = size // 2, size // 2
    
    # Draw two connected circles (Gemini symbol)
    circle_radius = 50
    offset = 30
    
    # Left circle (purple)
    left_circle = [center_x - offset - circle_radius, center_y - circle_radius,
                   center_x - offset + circle_radius, center_y + circle_radius]
    draw.ellipse(left_circle, fill=(147, 51, 255, 255), outline=(255, 255, 255, 255), width=4)
    
    # Right circle (pink)
    right_circle = [center_x + offset - circle_radius, center_y - circle_radius,
                    center_x + offset + circle_radius, center_y + circle_radius]
    draw.ellipse(right_circle, fill=(255, 20, 147, 255), outline=(255, 255, 255, 255), width=4)
    
    # Connection line
    draw.line([center_x - offset, center_y, center_x + offset, center_y], 
              fill=(255, 255, 255, 255), width=6)
    
    # Add sparkle/star effect
    star_size = 8
    stars = [
        (center_x - 60, center_y - 60),
        (center_x + 60, center_y - 60),
        (center_x - 60, center_y + 60),
        (center_x + 60, center_y + 60),
    ]
    for x, y in stars:
        draw.ellipse([x - star_size, y - star_size, x + star_size, y + star_size],
                     fill=(255, 255, 255, 200))
    
    return image

def save_icon_formats():
    """Save icon in multiple formats"""
    script_dir = Path(__file__).parent
    icon = create_app_icon()
    
    # Save as PNG (for preview)
    png_path = script_dir / "icon.png"
    icon.save(png_path, "PNG")
    print(f"[OK] Created icon.png: {png_path}")
    
    # Save as ICO (for Windows EXE)
    ico_path = script_dir / "icon.ico"
    # ICO needs multiple sizes
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    icon_images = []
    for size in sizes:
        resized = icon.resize(size, Image.Resampling.LANCZOS)
        icon_images.append(resized)
    
    icon_images[0].save(ico_path, format='ICO', sizes=[(s[0], s[1]) for s in sizes])
    print(f"[OK] Created icon.ico: {ico_path}")
    
    # Save as 64x64 PNG for system tray
    tray_icon = icon.resize((64, 64), Image.Resampling.LANCZOS)
    tray_path = script_dir / "tray_icon.png"
    tray_icon.save(tray_path, "PNG")
    print(f"[OK] Created tray_icon.png: {tray_path}")
    
    print("\nIcon created successfully!")
    print(f"Location: {script_dir}")
    print("\nNext steps:")
    print("1. Use icon.ico in build_exe.py")
    print("2. Use tray_icon.png for system tray (optional)")

if __name__ == "__main__":
    save_icon_formats()

