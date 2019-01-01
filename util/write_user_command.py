# coding=utf-8
import yaml


class WriteUserCommand:
    def read_data(self):
        """
        加载yaml数据
        :return: data
        """
        # withopen打开了文件忘记关闭会自动关闭
        with open("../config/userconfig.yaml") as fr:
            data = yaml.load(fr)
        return data

    def get_value(self, key, port):
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self, i, bp, device_name, port):
        data = self.join_data(i, bp, device_name, port)
        with open("../config/userconfig.yaml", "a") as fr:
            yaml.dump(data, fr)

    def join_data(self, i, bp, device_name, port):
        data = {
            "user_info_" + str(i): {
                "bp": bp,
                "deviceName": device_name,
                "port": port,
            }
        }
        return data

    def clear_data(self):
        with open("../config/userconfig.yaml", "w") as fr:
            fr.truncate()
        fr.close()

    def get_file_line(self):
        data = self.read_data()
        return len(data)


if __name__ == '__main__':
    write_file = WriteUserCommand()
    print write_file.get_value('user_info_0', 'bp')
