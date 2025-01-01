from word import Importance

class ColourCode:
    # Color constants
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    GREY = "\033[90m"
    RESET = "\033[0m"
    
    def __init__(self, is_matched: bool, importance: Importance):
        self.is_matched = is_matched
        self.importance = importance
        self.colour = self._get_colour()

    def _get_colour(self):
        if self.is_matched:
            if self.importance == Importance.HIGH:
                return self.GREEN
            return self.YELLOW
        if self.importance == Importance.HIGH:
            return self.RED
        return self.GREY

    def print(self, text, end="\n"):
        print(f"{self.colour}{text}{self.RESET}", end=end)

    def __str__(self):
        match_status = "Matched" if self.is_matched else "Unmatched"
        return f"{match_status} {self.importance.name} importance word"