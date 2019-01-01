# coding=utf-8
from dos_cmd import DosCmd


class Port:
    def port_is_used(self, port_num):
        flag = None
        self.dos = DosCmd()
        command = 'lsof -i:' + str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list):
        """
        根据device_list返回可用端口
        :param start_port:
        :param device_list:
        :return:
        """
        port_list = []
        if device_list is not None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) is False:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print "生成端口失败"
            # haha
            return None


if __name__ == '__main__':
    port = Port()
    device_list = [1, 2, 3, 4, 5]
    print port.create_port_list(4700, device_list)
