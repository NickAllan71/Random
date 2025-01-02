import argparse
from file_handler import FileHandler
from keyword_visualiser import KeywordVisualiser
from settings import Settings

GREEN = '\033[92m'
RESET = '\033[0m'

def get_folder_input(prompt, settings, key):
    default = settings.get(key)
    value = None
    while not value:
        value = input(f"{prompt} [{GREEN}{default or ''}{RESET}]: ").strip()
        if not value and default is not None:
            value = default
            break
    value = value if value else default
    if value:
        settings.set(key, value)
    return value

def get_paths():
    parser = argparse.ArgumentParser(description='Process job description and resume folders.')
    parser.add_argument('job_description_folder', type=str, nargs='?', help='Path to the job description folder')
    parser.add_argument('resume_folder', type=str, nargs='?', help='Path to the resume folder')
    args = parser.parse_args()

    settings = Settings()

    if not args.job_description_folder:
        args.job_description_folder = get_folder_input(
            "Job description folder",
            settings,
            'job_description_folder'
        )
    
    if not args.resume_folder:
        args.resume_folder = get_folder_input(
            "Resume folder",
            settings,
            'resume_folder'
        )
    
    unimportant_words_path = get_folder_input(
        "Unimportant words file",
        settings,
        'unimportant_words_path'
    )

    return args.job_description_folder, args.resume_folder, unimportant_words_path

if __name__ == "__main__":
    job_description_folder, resume_folder, unimportant_words_path = get_paths()
    file_handler = FileHandler(
        job_description_folder, 
        resume_folder, 
        recursive=True
    )
    match_results = list(file_handler.analyse())
    sorted_results = sorted(match_results, key=lambda x: x.match_score)

    for result in sorted_results:
        print(result)

    best_match = sorted_results[-1]
    keyword_visualiser = KeywordVisualiser(best_match.resume)
    keyword_visualiser.visualise()