import configparser
config = configparser.ConfigParser()

config.read('config_file.ini')
sample = config.get('text_file_required','file1')
print(sample)