# Ubuntu Image Fetcher

A Python script inspired by Ubuntu's principles of community and respect that allows users to download images from URLs while maintaining ethical web practices.

## Features

- **Multiple URL Support**: Download images from multiple URLs in a single session
- **Duplicate Detection**: Automatically prevents downloading the same image twice
- **Image Validation**: Ensures only valid image files are downloaded
- **Error Handling**: Graceful handling of network errors and invalid URLs
- **Progress Feedback**: Clear feedback on download progress and results
- **Organized Storage**: Creates a dedicated "Fetched_Images" directory for downloads

## Requirements

- Python 3.6 or higher
- `requests` library
- `Pillow` library

## Installation

1. Install required dependencies:
\`\`\`bash
pip install requests Pillow
\`\`\`

2. Run the script:
\`\`\`bash
python ubuntu_image_fetcher.py
\`\`\`

## Usage

1. Run the script and enter image URLs when prompted
2. Enter multiple URLs separated by commas, or one at a time
3. Type 'quit' or 'exit' to finish downloading
4. Images will be saved in the "Fetched_Images" directory

## Ubuntu Principles

This project embodies Ubuntu's core values:
- **Community**: Respectful interaction with web resources
- **Respect**: Proper error handling and user feedback
- **Collaboration**: Clean, readable code for community contribution

## File Structure

\`\`\`
├── ubuntu_image_fetcher.py    # Main image fetcher script
├── Fetched_Images/                # Downloaded images directory (created automatically)
└── README.md                      # This file
\`\`\`

## Error Handling

The script handles various scenarios:
- Invalid URLs
- Network connection issues
- Non-image content
- File system errors
- Duplicate downloads

## Contributing

Feel free to contribute improvements while maintaining the Ubuntu spirit of community and respect.
