# coding=utf-8
import sys

from get_data import GetData
from action_method import ActionMethod
from util.server import Server

sys.path.append('/Users/wei/Documents/PythonTest/AppiumPython')


class RunMain:
    def run_method(self):
        server = Server()
        server.main()
        data = GetData()
        action_method = ActionMethod()
        lines = data.get_case_lines()
        for i in range(1, lines):
            print "第" + str(i) + "行"
            # 获取处理步骤（input/click/等）
            handle_step = data.get_handle_step(i)
            # 拿需要操作的元素，比如一个文本框
            element_key = data.get_element_key(i)
            # 拿对需要操作元素操作的值，比如像文本框里输入值
            handle_value = data.get_handle_value(i)
            # 预期元素
            expect_key = data.get_expect_element(i)
            # 预期步骤
            expect_step = data.get_expect_handle(i)
            # 通过反射机制，通过获取的处理步骤拿到对应的方法，比如拿到了Input，就需要对XX元素输入xx值
            excute_method = getattr(action_method, handle_step)
            if element_key is not None:
                excute_method(element_key, handle_value)
            else:
                print handle_value
                excute_method(handle_value)

            if expect_step is not None:
                print "this is exepect_step:" + expect_step
                # 如果预期步骤不为空，通过expect_key去获取元素的位置id (findelementbyId 的id ）
                expect_result = getattr(action_method, expect_step)
                result = expect_result(expect_key)
                if result:
                    data.write_value(i, "pass")
                else:
                    data.write_value(i, "fail")


if __name__ == '__main__':
    run = RunMain()
    run.run_method()
