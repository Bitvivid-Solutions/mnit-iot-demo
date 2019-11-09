import configparser


class IotConfigParser:
    def __init__(self, config_path):
        self.__config__= config = configparser.ConfigParser()
        self.__config__.read(config_path)

    def get_section(self, section_name):
        try:
            config_section = self.__config__[section_name]
            return config_section
        except Exception as e:
            print("Unable to get section", e)



