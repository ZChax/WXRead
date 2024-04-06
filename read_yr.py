# -*- coding: utf-8 -*-
# read_yr.py created by MoMingLog on 6/4/2024.
"""
【作者】MoMingLog
【创建时间】2024-04-06
【功能描述】
new Env("鱼儿阅读");
0 45 7-23 * * * read_mm.py

统一入口链接：http://h5.pyqvr23agj8.cn/pipa_read?upuid=2068422

如果进不去，可以先运行一下 “read_entry_url.py”，如果青龙任务添加成功，应该称为 “阅读入口”

请确认完整拉库，此脚本的配置不依赖环境变量（为了后序账号cookie添加、修改、删除方便一点）

配置【!!参考文件!!】在 config\yryd_example.yaml中，请先阅读其中的注释内容，把【必填】都填上就可以运行了

实际生效的【配置文件名】为：yryd.yaml（第一次没有，请创建或将上方的参考文件重命名）

参考文件每次拉库都会拉取，注意里面可能会添加新的内容（我也会尽量在已有的yryd.yaml自动化添加）

如果需要其他额外的配置，请详细的阅读对应的注释内容并配置

！！！不熟练的先拿小号测试！！！
"""

from script.v2.yryd_v2 import YRYDV2

if __name__ == '__main__':
    YRYDV2()
