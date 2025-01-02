import json
import os

class Settings:
    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        self._settings = self._load()
    
    def _load(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save(self):
        with open(self.settings_file, 'w') as f:
            json.dump(self._settings, f)
    
    def get(self, key, default=None):
        return self._settings.get(key, default)
    
    def set(self, key, value):
        self._settings[key] = value
        self.save()