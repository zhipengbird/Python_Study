#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-06 13:49:33
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import requests
import time

url = "https://aweme.snssdk.com/aweme/v1/feed/"

querystring = {"iid":"18744911739","ac":"4G","os_api":"18","app_name":"aweme",
"channel":"App Store","idfa":"594C1906-D009-4CCC-8DB1-8628CCC792BD",
"device_platform":"iphone","build_number":"16403",
"vid":"8A9EB98E-8441-475F-BDDC-5B216AA6DE30",
"openudid":"9635c68c16968bc6f13e5ba3fa8091047910a029",
"device_type":"iPhone7,2","app_version":"1.6.4",
"device_id":"40940037689","version_code":"1.6.4",
"os_version":"10.3.3","screen_width":"750","aid":"1128",
"count":"6","feed_style":"0","max_cursor":"0","min_cursor":"0",
"pull_type":"1","type":"0","user_id":"75084315985","volume":"0.25",
#"cp":"7ea0ab582e742e6ae1","as":"a145d7e2b22a5a5667",
# "ts":time.localtime()
}

headers = {
    'cache-control': "no-cache",
    'postman-token': "6f436853-a357-7458-781e-446fd5bd80a1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
