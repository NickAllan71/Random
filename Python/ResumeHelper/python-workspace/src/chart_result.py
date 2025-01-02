import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from word import Importance

class ChartResult:
    def __init__(self, match_result):
        self.match_result = match_result
        self.colors = {
            'matched': '#2ecc71',    # green
            'unmatched': '#e74c3c'   # red
        }
    
    def _calculate_stats(self):
        categories = {
            Importance.HIGH: {'matched': 0, 'unmatched': 0},
            Importance.MEDIUM: {'matched': 0, 'unmatched': 0}
        }
        
        for word in self.match_result.resume.words:
            if word.importance in categories:
                status = 'matched' if word.is_matched else 'unmatched'
                categories[word.importance][status] += 1
            
        return categories
    
    def plot(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        categories = self._calculate_stats()
        
        # Configure subplots
        for ax, (importance, data) in zip([ax1, ax2], 
                                        [(Importance.HIGH, categories[Importance.HIGH]),
                                         (Importance.MEDIUM, categories[Importance.MEDIUM])]):
            total = data['matched'] + data['unmatched']
            if total > 0:
                sizes = [data['matched'], data['unmatched']]
                wedges, texts = ax.pie(sizes,
                    colors=[self.colors['matched'], self.colors['unmatched']],
                    labels=[f'{s/total*100:.0f}%' if s > 0 else '' for s in sizes],
                    labeldistance=0.75,
                    wedgeprops=dict(width=0.3),
                    startangle=90,
                    counterclock=False)
                ax.set_title(f'{importance.name} Importance')
        
        # Add shared legend
        legend_elements = [
            Patch(facecolor=self.colors['matched'], label='Matched'),
            Patch(facecolor=self.colors['unmatched'], label='Unmatched')
        ]
        fig.legend(handles=legend_elements,
                  loc='center',
                  bbox_to_anchor=(0.5, 0),
                  ncol=2)
        
        plt.suptitle(f'Match Analysis: {self.match_result.match_score:.0%}')
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    from file_handler import FileHandler
    from keyword_visualiser import KeywordVisualiser
    from resume_analyser import ResumeAnalyser
    file_handler = FileHandler(r"input_files")
    job_description_file, resume_file = next(file_handler.discover())
    analyser = ResumeAnalyser()
    match_result = analyser.analyse(job_description_file, resume_file)
    visualiser = KeywordVisualiser(match_result.job_description)
    visualiser.print_legend()
    visualiser.visualise()
    print(match_result.statistics)
    chart = ChartResult(match_result)
    chart.plot()