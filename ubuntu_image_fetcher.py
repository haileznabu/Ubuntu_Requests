import requests
import os
from urllib.parse import urlparse
import hashlib
from pathlib import Path

def get_filename_from_url(url):
    """Extract filename from URL or generate a meaningful one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    # If no filename in URL, generate one based on URL hash
    if not filename or '.' not in filename:
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        filename = f"image_{url_hash}.jpg"
    
    return filename

def is_valid_image_content(response):
    """Check if the response contains valid image content."""
    content_type = response.headers.get('content-type', '').lower()
    valid_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/webp']
    
    return any(img_type in content_type for img_type in valid_types)

def file_already_exists(filepath, content):
    """Check if file with same content already exists to prevent duplicates."""
    if not os.path.exists(filepath):
        return False
    
    # Compare file hashes to detect duplicates
    existing_hash = hashlib.md5(open(filepath, 'rb').read()).hexdigest()
    new_hash = hashlib.md5(content).hexdigest()
    
    return existing_hash == new_hash

def fetch_single_image(url, directory="Fetched_Images"):
    """Fetch a single image from URL with comprehensive error handling."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print(f"Connecting to: {url}")
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        
        if not is_valid_image_content(response):
            print(f"✗ URL does not contain a valid image: {url}")
            return False
        
        filename = get_filename_from_url(url)
        filepath = os.path.join(directory, filename)
        
        if file_already_exists(filepath, response.content):
            print(f"⚠ Image already exists (duplicate detected): {filename}")
            return True
        
        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        file_size = len(response.content)
        print(f"✓ Successfully fetched: {filename} ({file_size:,} bytes)")
        print(f"✓ Image saved to {filepath}")
        return True
        
    except requests.exceptions.Timeout:
        print(f"✗ Connection timeout: {url}")
    except requests.exceptions.ConnectionError:
        print(f"✗ Connection failed: {url}")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP error {e.response.status_code}: {url}")
    except requests.exceptions.RequestException as e:
        print(f"✗ Request error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
    
    return False

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print("Embodying Ubuntu: 'I am because we are'\n")
    
    try:
        os.makedirs("Fetched_Images", exist_ok=True)
        print("Fetched_Images directory ready")
    except Exception as e:
        print(f"✗ Could not create directory: {e}")
        return
    
    print("\nOptions:")
    print("1. Enter a single image URL")
    print("2. Enter multiple URLs (separated by commas)")
    
    choice = input("\nChoose option (1 or 2): ").strip()
    
    if choice == "2":
        urls_input = input("\nPlease enter image URLs (separated by commas): ")
        urls = [url.strip() for url in urls_input.split(',') if url.strip()]
    else:
        url = input("\nPlease enter the image URL: ").strip()
        urls = [url] if url else []
    
    if not urls:
        print("✗ No URLs provided")
        return
    
    print(f"\nConnecting to the global community...")
    print(f"Processing {len(urls)} URL(s)\n")
    
    successful = 0
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] ", end="")
        if fetch_single_image(url):
            successful += 1
        print()  # Add spacing between downloads
    
    print(f"\nSummary: {successful}/{len(urls)} images successfully fetched")
    
    if successful > 0:
        print("\nConnection strengthened. Community enriched.")
        print("Ubuntu wisdom: Through sharing, we all grow stronger.")
    else:
        print("\nNo images were fetched, but the attempt honors the Ubuntu spirit of trying.")

if __name__ == "__main__":
    main()
