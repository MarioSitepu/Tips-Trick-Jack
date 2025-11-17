"""
AI HTML/CSS Generator
Menggunakan AI untuk generate HTML dan CSS secara dinamis
"""
import os
import re
from datetime import datetime


def extract_html_from_response(response_text):
    """Extract HTML content from AI response"""
    # Cari tag <html> atau <!DOCTYPE html>
    html_match = re.search(r'(<!DOCTYPE html>.*?</html>)', response_text, re.DOTALL | re.IGNORECASE)
    if html_match:
        return html_match.group(1)
    
    # Jika tidak ada tag html lengkap, cari content di antara tag
    html_match = re.search(r'(<html.*?</html>)', response_text, re.DOTALL | re.IGNORECASE)
    if html_match:
        return html_match.group(1)
    
    # Fallback: return as is (mungkin sudah clean HTML)
    return response_text.strip()


def extract_css_from_response(response_text):
    """Extract CSS content from AI response"""
    # Cari CSS di dalam <style> tag
    style_match = re.search(r'<style[^>]*>(.*?)</style>', response_text, re.DOTALL | re.IGNORECASE)
    if style_match:
        return style_match.group(1).strip()
    
    # Cari CSS di dalam ```css code blocks
    css_match = re.search(r'```css\s*(.*?)\s*```', response_text, re.DOTALL)
    if css_match:
        return css_match.group(1).strip()
    
    # Cari CSS di dalam ``` code blocks (tanpa label)
    code_match = re.search(r'```\s*(.*?)\s*```', response_text, re.DOTALL)
    if code_match:
        content = code_match.group(1).strip()
        # Check if it looks like CSS
        if '{' in content and '}' in content:
            return content
    
    # Fallback: return as is
    return response_text.strip()


def generate_with_openai(date_str, theme="modern", style="gradient"):
    """
    Generate HTML/CSS menggunakan OpenAI API
    Install: pip install openai
    """
    try:
        from openai import OpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return None, None
        
        client = OpenAI(api_key=api_key)
        
        prompt = f"""Generate a complete, modern HTML page with embedded CSS for a project dated {date_str}.

Requirements:
- Create a beautiful, responsive HTML page
- Use modern CSS with {style} styling
- Theme: {theme}
- Include header, main content sections, and footer
- Make it visually appealing with good color scheme
- Ensure it's mobile responsive
- Include the date {date_str} in the content

Return ONLY the HTML code with embedded <style> tag. No explanations, just the code."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # atau "gpt-4" untuk hasil lebih baik
            messages=[
                {"role": "system", "content": "You are an expert web developer. Generate clean, modern HTML and CSS code."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        full_response = response.choices[0].message.content
        
        # Extract HTML and CSS
        html_content = extract_html_from_response(full_response)
        css_content = extract_css_from_response(full_response)
        
        # Jika HTML tidak lengkap, tambahkan structure dasar
        if not html_content.startswith("<!DOCTYPE"):
            html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project - {date_str}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Jika CSS kosong, extract dari style tag di HTML
        if not css_content and "<style" in html_content:
            css_content = extract_css_from_response(html_content)
            # Remove style tag dari HTML
            html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        
        # Pastikan HTML link ke external CSS
        if '<link rel="stylesheet"' not in html_content:
            html_content = html_content.replace('</head>', '    <link rel="stylesheet" href="style.css">\n</head>')
        
        return html_content, css_content
        
    except ImportError:
        return None, None
    except Exception as e:
        print(f"OpenAI error: {e}")
        return None, None


def generate_with_ollama(date_str, theme="modern", style="gradient"):
    """
    Generate HTML/CSS menggunakan Ollama (AI Lokal)
    Install: pip install ollama
    Setup: https://ollama.ai
    """
    try:
        import ollama
        
        prompt = f"""Generate a complete, modern HTML page with CSS for a project dated {date_str}.

Create a beautiful, responsive HTML page with:
- Modern CSS with {style} styling
- Theme: {theme}
- Header, main content, and footer
- Good color scheme
- Mobile responsive
- Include date {date_str} in content

Return ONLY the HTML code with embedded <style> tag. No explanations."""

        response = ollama.generate(
            model="llama3.2",  # atau model lain yang sudah diinstall
            prompt=prompt,
            options={
                "temperature": 0.7,
                "num_predict": 2000
            }
        )
        
        full_response = response['response']
        
        # Extract HTML and CSS
        html_content = extract_html_from_response(full_response)
        css_content = extract_css_from_response(full_response)
        
        # Jika HTML tidak lengkap, tambahkan structure dasar
        if not html_content.startswith("<!DOCTYPE"):
            html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project - {date_str}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Extract CSS dari style tag jika ada
        if not css_content and "<style" in html_content:
            css_content = extract_css_from_response(html_content)
            html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        
        # Pastikan HTML link ke external CSS
        if '<link rel="stylesheet"' not in html_content:
            html_content = html_content.replace('</head>', '    <link rel="stylesheet" href="style.css">\n</head>')
        
        return html_content, css_content
        
    except ImportError:
        return None, None
    except Exception as e:
        print(f"Ollama error: {e}")
        return None, None


def generate_with_anthropic(date_str, theme="modern", style="gradient"):
    """
    Generate HTML/CSS menggunakan Anthropic Claude API
    Install: pip install anthropic
    """
    try:
        import anthropic
        
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            return None, None
        
        client = anthropic.Anthropic(api_key=api_key)
        
        prompt = f"""Generate a complete, modern HTML page with CSS for a project dated {date_str}.

Create a beautiful, responsive HTML page with:
- Modern CSS with {style} styling
- Theme: {theme}
- Header, main content, and footer
- Good color scheme
- Mobile responsive
- Include date {date_str} in content

Return ONLY the HTML code with embedded <style> tag. No explanations."""

        response = client.messages.create(
            model="claude-3-haiku-20240307",  # atau "claude-3-opus" untuk hasil lebih baik
            max_tokens=2000,
            temperature=0.7,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        full_response = response.content[0].text
        
        # Extract HTML and CSS
        html_content = extract_html_from_response(full_response)
        css_content = extract_css_from_response(full_response)
        
        # Jika HTML tidak lengkap, tambahkan structure dasar
        if not html_content.startswith("<!DOCTYPE"):
            html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project - {date_str}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Extract CSS dari style tag jika ada
        if not css_content and "<style" in html_content:
            css_content = extract_css_from_response(html_content)
            html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        
        # Pastikan HTML link ke external CSS
        if '<link rel="stylesheet"' not in html_content:
            html_content = html_content.replace('</head>', '    <link rel="stylesheet" href="style.css">\n</head>')
        
        return html_content, css_content
        
    except ImportError:
        return None, None
    except Exception as e:
        print(f"Anthropic error: {e}")
        return None, None


def generate_with_gemini(date_str, theme="modern", style="gradient"):
    """
    Generate HTML/CSS menggunakan Google Gemini 2.5 Flash
    Install: pip install google-generativeai
    """
    try:
        import google.generativeai as genai
        
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return None, None
        
        genai.configure(api_key=api_key)
        
        # Gunakan Gemini 2.5 Flash (atau fallback ke versi lain)
        models_to_try = [
            'gemini-2.5-flash',        # Stable Gemini 2.5 Flash (Recommended)
            'gemini-2.0-flash-001',    # Stable Gemini 2.0 Flash
            'gemini-2.0-flash',        # Gemini 2.0 Flash
            'gemini-flash-latest',     # Latest Flash
        ]
        
        model = None
        for model_name in models_to_try:
            try:
                model = genai.GenerativeModel(model_name)
                # Test dengan simple request
                model.generate_content("test", generation_config=genai.types.GenerationConfig(max_output_tokens=1))
                break
            except Exception as e:
                # Try next model
                continue
        
        if not model:
            raise Exception("No available Gemini model found")
        
        prompt = f"""Generate a complete, modern HTML page with embedded CSS for a project dated {date_str}.

Requirements:
- Create a beautiful, responsive HTML page
- Use modern CSS with {style} styling
- Theme: {theme}
- Include header, main content sections, and footer
- Make it visually appealing with good color scheme
- Ensure it's mobile responsive
- Include the date {date_str} in the content
- Return ONLY the HTML code with embedded <style> tag
- No explanations, just the code

Format: Return HTML with <style> tag inside <head> section."""

        # Safety settings - allow more content
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=4000,  # Increased for HTML/CSS
            ),
            safety_settings=safety_settings
        )
        
        # Handle response properly
        if not response.candidates:
            raise Exception("No candidates in response")
        
        candidate = response.candidates[0]
        
        # Check finish reason
        finish_reason = candidate.finish_reason
        # 1 = STOP (success), 2 = MAX_TOKENS, 3 = SAFETY, 4 = RECITATION, 5 = OTHER
        if finish_reason == 3:  # SAFETY
            raise Exception("Content blocked by safety filter")
        elif finish_reason == 4:  # RECITATION
            raise Exception("Content blocked due to recitation")
        
        # Try to get text even if finish_reason is not STOP
        try:
            full_response = response.text
        except:
            # Fallback: try to get content from parts
            if candidate.content and candidate.content.parts:
                full_response = "".join([part.text for part in candidate.content.parts if hasattr(part, 'text')])
            else:
                raise Exception(f"Could not extract text. Finish reason: {finish_reason}")
        
        # Extract HTML and CSS
        html_content = extract_html_from_response(full_response)
        css_content = extract_css_from_response(full_response)
        
        # Jika HTML tidak lengkap, tambahkan structure dasar
        if not html_content.startswith("<!DOCTYPE"):
            html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project - {date_str}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Extract CSS dari style tag jika ada
        if not css_content and "<style" in html_content:
            css_content = extract_css_from_response(html_content)
            html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        
        # Pastikan HTML link ke external CSS
        if '<link rel="stylesheet"' not in html_content:
            html_content = html_content.replace('</head>', '    <link rel="stylesheet" href="style.css">\n</head>')
        
        return html_content, css_content
        
    except ImportError:
        return None, None
    except Exception as e:
        print(f"Gemini error: {e}")
        return None, None


def generate_html_css_with_ai(date_str, ai_provider="auto", theme="modern", style="gradient"):
    """
    Generate HTML/CSS menggunakan AI
    
    Args:
        date_str: Tanggal untuk project
        ai_provider: "gemini", "openai", "ollama", "anthropic", atau "auto" (coba semua)
        theme: Tema design (modern, classic, minimal, dark, dll)
        style: Style CSS (gradient, solid, glassmorphism, dll)
    
    Returns:
        tuple: (html_content, css_content) atau (None, None) jika gagal
    """
    
    providers = []
    if ai_provider == "auto":
        # Coba semua provider yang tersedia, Gemini pertama
        providers = ["gemini", "openai", "ollama", "anthropic"]
    else:
        providers = [ai_provider]
    
    for provider in providers:
        try:
            if provider == "gemini":
                html, css = generate_with_gemini(date_str, theme, style)
                if html and css:
                    return html, css
            elif provider == "openai":
                html, css = generate_with_openai(date_str, theme, style)
                if html and css:
                    return html, css
            elif provider == "ollama":
                html, css = generate_with_ollama(date_str, theme, style)
                if html and css:
                    return html, css
            elif provider == "anthropic":
                html, css = generate_with_anthropic(date_str, theme, style)
                if html and css:
                    return html, css
        except Exception as e:
            print(f"Error with {provider}: {e}")
            continue
    
    return None, None

