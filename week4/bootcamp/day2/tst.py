import configparser
config = configparser.ConfigParser()

config.read('config_file.ini')
sample = config.get('text_file_required','file1')
with open(sample, "r") as f:
    print(f.read())

# data = open('event.yaml', 'r+')
# a = configparser.ConfigParser()
# a.read_file(data)
# print(a)