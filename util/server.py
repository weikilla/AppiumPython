# coding=utf-8
import time

from dos_cmd import DosCmd
from port import Port
import threading
from util.write_user_command import WriteUserCommand


class Server:

    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.write_file = WriteUserCommand()

    def get_devices(self):
        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port_list(self, start_port):
        """
        只需传入start_port，生成端口号
        :param start_port:
        :return:返回port_list
        """
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        """
        批量生成
        appium -p 4700 -bp 4701 -U 127.0.0.1:21503
        :return:
        """

        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        devices_list = self.get_devices()
        command = 'appium -p ' + str(appium_port_list[i]) + ' -bp ' + str(bootstrap_port_list[i]) + ' -U ' + str(
            devices_list[i]) + ' --no-reset --session-override'
        command_list.append(command)
        self.write_file.write_data(i, bootstrap_port_list[i], devices_list[i], appium_port_list[i])
        return command_list

    def start_server(self, i):
        """
        循环执行命令
        :return:
        """
        self.start_list = self.create_command_list(i)
        print self.start_list
        self.dos.excute_cmd(self.start_list[0])

    def kill_server(self):
        server_list = self.dos.excute_cmd_result('ps aux|grep node')
        if len(server_list) > 0:
            self.dos.excute_cmd('killall -9 node')

    def main(self):
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start.start()
        time.sleep(20)


if __name__ == '__main__':
    server = Server()
    print server.main()
