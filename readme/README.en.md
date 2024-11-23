<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_django_serializer/readme/README.en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_serializer

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## Description

Based on the djangorestframework's serializer parsing base class, it encapsulates common functions for easy and rapid development.

## Source Code Repositories

| [Github](https://github.com/xy-web-service/xy_django_serializer.git)         | [Gitee](https://gitee.com/xy-opensource/xy_django_serializer.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_django_serializer.git)          |
| ----------- | -------------|---------------------------------------|


## Installation

```bash
# bash
pip install xy_django_serializer
```

## How to use

#### 1. Creating a parsing class

```python
# serializers.py

from rest_framework import viewsets
from xy_django_serializer.serializers import Serializer

from .models import MImage


class SImage(Serializer):
    default_value = ""

    class Meta:
        model = MImage
        fields = "__all__"

class VSImage(viewsets.ModelViewSet):
    queryset = MImage.objects.all()
    serializer_class = SImage

```

#### 2. Implementation analysis

###### 1. Call in the manage.py shell of the Django project

```python
# Python解释器
from Demo.models import MDemo
from Demo.serializers import SDemo

demo_list = MDemo.objects.all()
demo_dict_list = SDemo(demo_list, many=True).data
print(demo_list)
print(demo_dict_list))
```

###### 2. Calling in other runtime environments such as Tornado
> <b>Tip:</b> You must first load the Django project into the running project

```Python
# Demoes.py
from xy_request_handler_api.Api import Api
from Demo.models import MDemo
from Demo.serializers import SDemo

class DemoApi(Api):
    def check_xsrf_cookie(self) -> None:
        return None

    def check_origin(self, _):
        return False

    def fetch(self):
        all_demo_list = MDemo.objects.all()
        all_demo_dict_list = SDemo(all_demo_list, many=True).data
        self.success()
        self.data = {"all_demo_list": all_demo_dict_list}
        self.xy_response()

    def get(self):
        self.fetch()

    def post(self):
        self.fetch()

```

##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b> 

| [Github](https://github.com/xy-web-service/xy_web_server.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_server.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_server.git)          |
| ----------- | -------------|---------------------------------------|

## License
xy_django_serializer is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![pay-total](./pay-total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```