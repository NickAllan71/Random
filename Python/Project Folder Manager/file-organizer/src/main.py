import sys
from utils.file_handler import FileHandler

def main():
    print(sys.argv)

    if len(sys.argv) != 3:
        print("Usage: python main.py <FolderPath> <FileSpec>")
        sys.exit(1)

    folder_path = sys.argv[1]
    file_spec = sys.argv[2]

    try:
        file_handler = FileHandler(folder_path, file_spec)
        processed_files = file_handler.process()
        
        if processed_files:
            print(f"Processed {len(processed_files)} files")
        else:
            print("No matching files found")
            
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()