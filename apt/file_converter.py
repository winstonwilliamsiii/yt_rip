from moviepy.editor import VideoFileClip
import os
from file_converter import convert_to_mp3

def convert_to_mp3(filename):
    try:
        # Validate file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Video file not found: {filename}")
            
        # Check if file is video format
        valid_formats = ['.mp4', '.avi', '.mov', '.mkv']
        if not any(filename.lower().endswith(fmt) for fmt in valid_formats):
            raise ValueError(f"Unsupported video format. Use: {', '.join(valid_formats)}")
            
        # Create output filename
        output_file = filename[:-4] + ".mp3"
        
        # Convert to MP3
        clip = VideoFileClip(filename)
        clip.audio.write_audiofile(output_file)
        clip.close()
        
        return output_file
        
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        return None
    finally:
        # Ensure clip is closed even if error occurs
        if 'clip' in locals():
            clip.close()

result = convert_to_mp3("test_video.mp4")
if result:
    print(f"Successfully converted to: {result}")
else:
    print("Conversion failed")
