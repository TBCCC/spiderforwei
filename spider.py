#!/usr/bin/env python
# -*- coding:UTF-8 -*-


import re
import urllib
import urllib2
import sys
# from bs4 import BeautifulSoup


reload(sys)
sys.setdefaultencoding('utf8')

url = "http://cc.seu.edu.cn/zscx/default.aspx"
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}


def get_post_data():
    '''
    获取所需的post参数
    '''
    namenum = str(raw_input("输入姓名或者身份证号码："))
    url = "http://cc.seu.edu.cn/zscx/default.aspx"
    headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    page = response.read()
    get_VIEWSTATEGENERATOR_pattern = re.compile(
        r'<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)"')
    __VIEWSTATEGENERATOR = re.findall(
        get_VIEWSTATEGENERATOR_pattern, page)[0]
    get_VIEWSTATEENCRYPTED_pattern = re.compile(
        r'<input type="hidden" name="__VIEWSTATEENCRYPTED" id="__VIEWSTATEENCRYPTED" value="(.*?)"')
    __VIEWSTATEENCRYPTED = re.findall(
        get_VIEWSTATEENCRYPTED_pattern, page)[0]
    get_VIEWSTATE_pattern = re.compile(
        r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)"')
    __VIEWSTATE = re.findall(
        get_VIEWSTATE_pattern, page)[0]
    get_EVENTVALIDATION_pattern = re.compile(
        r'<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)"')
    __EVENTVALIDATION = re.findall(
        get_EVENTVALIDATION_pattern, page)[0]

    # return __VIEWSTATEGENERATOR, __VIEWSTATEENCRYPTED, __VIEWSTATE,
    # __EVENTVALIDATION
    data = {
        "Button1": "查询",
        "TextBox1": namenum,
        "__EVENTVALIDATION": __EVENTVALIDATION,
        "__VIEWSTATE": __VIEWSTATE,
        "__VIEWSTATEENCRYPTED": __VIEWSTATEENCRYPTED,
        "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR

    }
    return data


def clear_data(read):
    try:
        get_num_pattern = re.compile(
            r'<span id="DataList1_ctl00_zkzhLabel">(.*?)<')
        num = re.findall(
            get_num_pattern, read)[0]
        get_idcard_pattern = re.compile(
            r'<span id="DataList1_ctl00_zjhLabel">(.*?)<')
        idcard = re.findall(
            get_idcard_pattern, read)[0]
        get_time_pattern = re.compile(
            r'<span id="DataList1_ctl00_ksnyLabel">(.*?)<')
        time = re.findall(
            get_time_pattern, read)[0]
        get_name_pattern = re.compile(
            r'<span id="DataList1_ctl00_xmLabel">(.*?)<')
        name = re.findall(
            get_name_pattern, read)[0]
        print "准考证号：%s" % num
        print "学生姓名：%s" % name
        print "身份证号：%s" % idcard
        print "考试时间：%s" % time
    except IndexError as e:
        print "没有查询到证书或者没有正确输入"


if __name__ == '__main__':
    values = get_post_data()
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data, headers=headers)
    response = urllib2.urlopen(request)
    read = response.read()
    clear_data(read)
