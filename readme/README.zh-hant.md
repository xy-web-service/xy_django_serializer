<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_django_serializer/readme/README.zh-hant.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_serializer

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## 說明

基於djangorestframework的serializer解析基底類別, 封裝了常用功能, 方便快速開發.

## 程式碼庫

| [Github](https://github.com/xy-web-service/xy_django_serializer.git)         | [Gitee](https://gitee.com/xy-opensource/xy_django_serializer.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_django_serializer.git)          |
| ----------- | -------------|---------------------------------------|


## 安裝

```bash
# bash
pip install xy_django_serializer
```

## 使用


#### 1. 建立解析類別

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

#### 2. 實作解析

###### 1. 在Django專案的manage.py shell中調用

```python
# Python解释器
from Demo.models import MDemo
from Demo.serializers import SDemo

demo_list = MDemo.objects.all()
demo_dict_list = SDemo(demo_list, many=True).data
print(demo_list)
print(demo_dict_list))
```

###### 2. 在Tornado等其他運行環境中調用
> <b>注意:</b> 必須先載入Django工程到運行的專案中

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

##### 運轉 [範例工程](../samples/xy_web_server_demo)

> 範例工程具體使用方式請移步 <b style="color: blue">xy_web_server.git</b> 下列倉庫

| [Github](https://github.com/xy-web-service/xy_web_server.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_server.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_server.git)          |
| ----------- | -------------|---------------------------------------|

## 許可證
xy_django_serializer 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![pay-total](./pay-total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```