import matplotlib.pyplot as plt
import os

class ResultsChart:
    def __init__(self, results):
        self.results = results
        
    def plot(self):
        # Prepare data
        scores = [result.match_score * 100 for result in self.results]
        labels = [os.path.basename(result.resume.file_path) for result in self.results]
        colors = ['#2ecc71' if score >= 70 else '#f1c40f' if score >= 50 else '#e74c3c' 
                 for score in scores]

        # Create bar chart
        plt.figure(figsize=(10, 6))
        bars = plt.bar(labels, scores, color=colors)
        
        # Customize chart
        plt.title('Resume Match Scores')
        plt.xlabel('Resume')
        plt.ylabel('Match Score (%)')
        plt.xticks(rotation=45, ha='right')
        plt.ylim(0, 100)
        
        # Add score labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom')
            
        plt.tight_layout()
        plt.show()

# Usage in file_handler.py:
if __name__ == '__main__':
    from chart_results import ResultsChart
    from file_handler import FileHandler
    file_handler = FileHandler(
        job_description_folder=r"C:\Users\Nick\Dropbox\Job Hunting\Applications\In Progress\Data Warehouse Developer - T-SQL, SSIS by Tenth Revolution Group in London Ref- 222850916",
        resume_folder=r"C:\Users\Nick\Dropbox\Job Hunting\Applications",
        unimportant_words_file_path=r"input_files\unimportant_words.txt",
        recursive=True
    )
    results = list(file_handler.analyse())
    
    # Create and show chart
    chart = ResultsChart(results)
    chart.plot()