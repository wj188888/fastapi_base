# -*- coding: utf-8 -*-
import requests
import pytest

class TestA:
    def setup(self):
        self.g = globals()
        self.s = requests.session()

    def test_a(self):
        """用例a"""
        result_a = "aaa" # 用例a的返回值

        self.g["a"] = result_a
        assert result_a == "aaa"

    def test_b(self):
        """用例b"""
        res_a = self.g["a"] # 引用用例a的返回值
        print(f"用例b引用用例a的返回值{res_a}")
        result_b = res_a + "111"
        self.g["b"] = result_b
        assert result_b == "aaa111"

    def test_c(self):
        """用例c"""
        print(f"用例c依赖用力a和用例b")

        c_a = self.g["a"]
        c_b = self.g["b"]
        enter = "\t"
        print(f"用例c请求的入参a:{enter}{c_a}")
        print(f"用例c请求的入参b:{enter}{c_b}")

